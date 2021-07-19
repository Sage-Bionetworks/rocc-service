import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError
from mongoengine.queryset.visitor import Q
import traceback
import datetime

from openapi_server.dbmodels.challenge import Challenge as DbChallenge
from openapi_server.dbmodels.challenge_platform import ChallengePlatform as DbChallengePlatform  # noqa: E501
# from openapi_server.dbmodels.challenge_results import ChallengeResults as DbChallengeResults  # noqa: E501
from openapi_server.dbmodels.grant import Grant as DbGrant
from openapi_server.dbmodels.person import Person as DbPerson
from openapi_server.dbmodels.organization import Organization as DbOrganization
from openapi_server.dbmodels.tag import Tag as DbTag
from openapi_server.models.challenge import Challenge
from openapi_server.models.challenge_create_response import ChallengeCreateResponse  # noqa: E501
from openapi_server.models.error import Error
from openapi_server.models.page_of_challenges import PageOfChallenges
from openapi_server.config import Config


def create_challenge():
    """Add a challenge

    Adds a challenge

    :rtype: Challenge
    """
    res = None
    status = None
    try:
        if connexion.request.is_json:
            challenge = Challenge.from_dict(connexion.request.get_json())

            for tag_id in challenge.tag_ids:
                try:
                    DbTag.objects.get(id=tag_id)
                except DoesNotExist:
                    status = 400
                    res = Error(f"The tag {tag_id} was not found", status)
                    return res, status

            for person_id in challenge.organizer_ids:
                try:
                    DbPerson.objects.get(id=person_id)
                except DoesNotExist:
                    status = 400
                    res = Error(f"The person {person_id} was not found", status)  # noqa: E501
                    return res, status

            for data_provider_id in challenge.data_provider_ids:
                try:
                    DbOrganization.objects.get(id=data_provider_id)
                except DoesNotExist:
                    status = 400
                    res = Error(f"The data provider {data_provider_id} was not found", status)  # noqa: E501
                    return res, status

            for grant_id in challenge.grant_ids:
                try:
                    DbGrant.objects.get(id=grant_id)
                except DoesNotExist:
                    status = 400
                    res = Error(f"The grant {grant_id} was not found", status)
                    return res, status

            try:
                DbChallengePlatform.objects.get(id=challenge.platform_id)
            except DoesNotExist:
                status = 400
                res = Error(f"The challenge platform {challenge.platform_id} was not found", status)  # noqa: E501
                return res, status

            try:
                db_challenge = DbChallenge(
                    name=challenge.name,
                    description=challenge.description,
                    summary=challenge.summary,
                    startDate=challenge.start_date,
                    endDate=challenge.end_date,
                    url=challenge.url,
                    status=challenge.status,
                    tagIds=challenge.tag_ids,
                    organizerIds=challenge.organizer_ids,
                    dataProviderIds=challenge.data_provider_ids,
                    grantIds=challenge.grant_ids,
                    platformId=challenge.platform_id
                    # challengeResults=DbChallengeResults(
                    #     nSubmissions=challenge.challenge_results.n_submissions,  # noqa: E501
                    #     nFinalSubmissions=challenge.challenge_results.n_final_submissions,  # noqa: E501
                    #     nRegisteredParticipants=challenge.challenge_results.n_registered_participants,  # noqa: E501
                    # ),
                ).save(force_insert=True)
                new_id = db_challenge.to_dict().get("id")
                res = ChallengeCreateResponse(id=new_id)
                status = 201
            except NotUniqueError as error:
                status = 409
                res = Error("Conflict", status, str(error))
        else:
            status = 400
            res = Error("Bad request", status)
    except Exception as error:
        traceback.print_exc()
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def delete_challenge(challenge_id):
    """Delete a challenge

    Deletes the challenge specified

    :param challenge_id: The ID of the challenge
    :type challenge_id: str

    :rtype: Challenge
    """
    res = None
    status = None
    try:
        DbChallenge.objects.get(id=challenge_id).delete()
        res = {}
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def get_challenge(challenge_id):
    """Get a challenge

    Returns the challenge specified

    :param challenge_id: The ID of the challenge
    :type challenge_id: str

    :rtype: Challenge
    """
    res = None
    status = None
    try:
        db_challenge = DbChallenge.objects.get(id=challenge_id)
        res = Challenge.from_dict(db_challenge.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def list_challenges(limit=None, offset=None, sort=None, direction=None, search_terms=None, tag_ids=None, status=None, platform_ids=None, start_date_range=None):  # noqa: E501
    """List all the challenges

    Returns all the challenges # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int
    :param sort: Property used to sort the results that must be returned
    :type sort: str
    :param direction: Can be either &#x60;asc&#x60; or &#x60;desc&#x60;. Ignored without &#x60;sort&#x60; parameter.
    :type direction: str
    :param search_terms: A string of search terms used to filter the results
    :type search_terms: str
    :param tag_ids: Array of tag ids used to filter the results
    :type tag_ids: List[str]
    :param status: Array of challenge status used to filter the results
    :type status: list | bytes
    :param platform_ids: Array of challenge platform ids used to filter the results
    :type platform_ids: List[str]
    :param start_date_range: Return challenges that start during the date range specified
    :type start_date_range: dict | bytes

    :rtype: PageOfChallenges
    """
    res = None
    status_ = None
    try:
        print('date range:', start_date_range)
        start_date_start = None
        start_date_end = None
        if start_date_range is not None and 'start' in start_date_range:
            print('start', start_date_range['start'])
            start_date_start = datetime.datetime.strptime(start_date_range['start'], '%Y-%m-%d')  # noqa: E501
            print('start result', start_date_start)
        if start_date_range is not None and 'end' in start_date_range:
            start_date_end = datetime.datetime.strptime(start_date_range['end'], '%Y-%m-%d')  # noqa: E501

        print('past bed time')

        status_q = Q(status__in=status) \
            if status is not None else Q()
        tag_ids_q = Q(tagIds__in=tag_ids) \
            if tag_ids is not None and len(tag_ids) > 0 else Q()
        platform_id_q = Q(platformId__in=platform_ids) \
            if platform_ids is not None and len(platform_ids) > 0 else Q()
        startDate_start_q = Q(startDate__gte=start_date_start) \
            if start_date_start is not None else Q()
        startDate_end_q = Q(startDate__lte=start_date_end) \
            if start_date_end is not None else Q()

        db_challenges = DbChallenge.objects(
            status_q & tag_ids_q & platform_id_q & startDate_start_q & startDate_end_q  # noqa: E501
        ).skip(offset).limit(limit)

        if search_terms is not None:
            db_challenges = db_challenges.search_text(search_terms)

        if sort is not None:
            order_by = ('-' if direction == 'desc' else '') + sort
            db_challenges = db_challenges.order_by(order_by)

        challenges = [Challenge.from_dict(d.to_dict()) for d in db_challenges]
        next_ = ""
        if len(challenges) == limit:
            next_ = "%s/challenges?limit=%s&offset=%s" % \
                (Config().server_api_url, limit, offset + limit)

        # Get total results count.
        total = db_challenges.count()

        res = PageOfChallenges(
            offset=offset,
            limit=limit,
            paging={
                "next": next_
            },
            total_results=total,
            challenges=challenges)
        status_ = 200
    except TypeError:  # TODO: may need different exception
        status_ = 400
        res = Error("Bad request", status_)
    except Exception as error:
        status_ = 500
        res = Error("Internal error", status_, str(error))
    return res, status_


def delete_all_challenges():
    """Delete all challenges

    Delete all challenges

    :rtype: object
    """
    res = None
    status = None
    try:
        DbChallenge.objects.delete()
        res = {}
        status = 200
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status
