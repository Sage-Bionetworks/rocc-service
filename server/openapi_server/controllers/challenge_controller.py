import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError
from mongoengine.queryset.visitor import Q
import traceback

from openapi_server.dbmodels.challenge import Challenge as DbChallenge
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
                    grantIds=challenge.grant_ids
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


def list_challenges(limit=None, offset=None, filter_=None, sort=None, direction=None):  # noqa: E501
    """List all the challenges

    Returns all the challenges # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int
    :param filter: Object that describes how to filter the results
    :type filter: dict | bytes
    :param sort: Property used to sort the results that must be returned
    :type sort: str
    :param direction: Can be either &#x60;asc&#x60; or &#x60;desc&#x60;. Ignored without &#x60;sort&#x60; parameter.
    :type direction: str

    :rtype: PageOfChallenges
    """
    res = None
    status = None
    try:
        # Get results based on query, limit and offset.
        name_q = Q(name__icontains=filter_['name']) \
            if 'name' in filter_ else Q()
        status_q = Q(status=filter_['status']) \
            if 'status' in filter_ else Q()
        organizer_q = Q(organizerIds__contains=filter_['organizer']) \
            if 'organizer' in filter_ else Q()
        tag_q = Q(tagIds__contains=filter_['tag']) \
            if 'tag' in filter_ else Q()

        order_by = 'createdAt'  # TODO: what is the best default behavior?
        if sort is not None:
            order_by = ('-' if direction == 'desc' else '') + sort

        db_challenges = DbChallenge.objects(
            name_q & status_q & organizer_q & tag_q
        ).skip(offset).limit(limit).order_by(order_by)
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
        status = 200
    except TypeError:  # TODO: may need different exception
        status = 400
        res = Error("Bad request", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


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
