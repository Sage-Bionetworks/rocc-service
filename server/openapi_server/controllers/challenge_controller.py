import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError
from mongoengine.queryset.visitor import Q
import datetime

from openapi_server.dbmodels.account import Account as DbAccount
from openapi_server.dbmodels.challenge import Challenge as DbChallenge
from openapi_server.dbmodels.challenge_platform import ChallengePlatform as DbChallengePlatform  # noqa: E501
from openapi_server.dbmodels.challenge_organizer import ChallengeOrganizer as DbChallengeOrganizer  # noqa: E501
from openapi_server.dbmodels.challenge_readme import ChallengeReadme as DbChallengeReadme  # noqa: E501
from openapi_server.dbmodels.starred_challenge import StarredChallenge as DbStarredChallenge  # noqa: E501
from openapi_server.dbmodels.user import User as DbUser  # noqa: E501
from openapi_server.models.challenge import Challenge  # noqa: E501
from openapi_server.models.challenge_create_request import ChallengeCreateRequest  # noqa: E501
from openapi_server.models.challenge_create_response import ChallengeCreateResponse  # noqa: E501
from openapi_server.models.challenge_readme import ChallengeReadme  # noqa: E501
from openapi_server.models.challenge_readme_update_request import ChallengeReadmeUpdateRequest  # noqa: E501
from openapi_server.models.challenge_organizer import ChallengeOrganizer  # noqa: E501
from openapi_server.models.challenge_organizer_create_request import ChallengeOrganizerCreateRequest  # noqa: E501
from openapi_server.models.challenge_organizer_create_response import ChallengeOrganizerCreateResponse  # noqa: E501
from openapi_server.models.challenge_organizer_list import ChallengeOrganizerList  # noqa: E501
from openapi_server.models.user import User
from openapi_server.models.array_of_topics import ArrayOfTopics  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_challenges import PageOfChallenges  # noqa: E501
from openapi_server.models.page_of_users import PageOfUsers  # noqa: E501
from openapi_server.config import config


def create_challenge(account_name):  # noqa: E501
    """Add a challenge

    Adds a challenge # noqa: E501

    :param account_name: The name of the account that owns the challenge
    :type account_name: str

    :rtype: ChallengeCreateResponse
    """
    if connexion.request.is_json:
        try:
            try:
                account = DbAccount.objects.get(login=account_name)
                account_id = account.to_dict().get("id")
            except DoesNotExist:
                status = 400
                res = Error(f"The account {account_name} was not found", status)  # noqa: E501
                return res, status

            challenge_create_request = ChallengeCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501
            platform_id = challenge_create_request.platform_id

            try:
                DbChallengePlatform.objects.get(id=platform_id)
            except DoesNotExist:
                status = 400
                res = Error(f"The challenge platform {platform_id} was not found", status)  # noqa: E501
                return res, status

            challenge = DbChallenge(
              name=challenge_create_request.name,
              displayName=challenge_create_request.display_name,
              description=challenge_create_request.description,
              websiteUrl=challenge_create_request.website_url,
              status=challenge_create_request.status,
              startDate=challenge_create_request.start_date,
              endDate=challenge_create_request.end_date,
              platformId=challenge_create_request.platform_id,
              topics=challenge_create_request.topics,
              doi=challenge_create_request.doi,
              fullName="%s/%s" % (account_name, challenge_create_request.name),
              ownerId=account_id
            ).save()
            challenge_id = challenge.to_dict().get("id")

            DbChallengeReadme(
                text=challenge_create_request.name,
                challengeId=challenge_id
            ).save()

            res = ChallengeCreateResponse(id=challenge_id)
            status = 201
        except NotUniqueError as error:
            status = 409
            res = Error("Conflict", status, str(error))
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))
    else:
        status = 400
        res = Error("Bad request", status, "Missing body")
    return res, status


def delete_all_challenges():  # noqa: E501
    """Delete all challenges

    Delete all challenges # noqa: E501


    :rtype: object
    """
    try:
        DbChallengeReadme.objects.delete()
        DbChallenge.objects.delete()
        res = {}
        status = 200
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def delete_challenge(account_name, challenge_name):  # noqa: E501
    """Delete a challenge

    Deletes the challenge specified # noqa: E501

    :param account_name: The name of the account that owns the challenge
    :type account_name: str
    :param challenge_name: The name of the challenge
    :type challenge_name: str

    :rtype: object
    """
    try:
        account = DbAccount.objects.get(login=account_name)
        account_id = account.to_dict().get("id")
        db_challenge = DbChallenge.objects.get(owner_id=account_id, name=challenge_name)  # noqa: E501
        challenge_id = db_challenge.to_dict().get("id")

        # delete readme
        DbChallengeReadme.objects.get(challengeId=challenge_id).delete()

        # delete organizers

        db_challenge.delete()
        res = {}
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def get_challenge(account_name, challenge_name):  # noqa: E501
    """Get a challenge

    Returns the challenge specified # noqa: E501

    :param account_name: The name of the account that owns the challenge
    :type account_name: str
    :param challenge_name: The name of the challenge
    :type challenge_name: str

    :rtype: Challenge
    """
    try:
        account = DbAccount.objects.get(login=account_name)
        account_id = account.to_dict().get("id")
        db_challenge = DbChallenge.objects.get(ownerId=account_id, name=challenge_name)  # noqa: E501
        res = Challenge.from_dict(db_challenge.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def list_account_challenges(account_name, limit=None, offset=None):  # noqa: E501
    """List all the challenges owned by the specified account

    List all the challenges owned by the specified account # noqa: E501

    :param account_name: The name of the account that owns the challenge
    :type account_name: str
    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfChallenges
    """
    try:
        account = DbAccount.objects.get(login=account_name)
        account_id = account.to_dict().get("id")
        db_challenges = DbChallenge.objects(ownerId=account_id).skip(offset).limit(limit)  # noqa: E501
        challenges = [Challenge.from_dict(d.to_dict()) for d in db_challenges]
        next_ = ""
        if len(challenges) == limit:
            next_ = "%s/challenges/%s?limit=%s&offset=%s" % \
                (config.server_api_url, account_name, limit, offset + limit)

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
    except TypeError:  # TODO: may need include different exceptions for 400
        status = 400
        res = Error("Bad request", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def list_challenge_stargazers(account_name, challenge_name, limit=None, offset=None):  # noqa: E501
    """List stargazers

    Lists the people that have starred the repository. # noqa: E501

    :param account_name: The name of the account that owns the challenge
    :type account_name: str
    :param challenge_name: The name of the challenge
    :type challenge_name: str
    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfUsers
    """
    try:
        try:
            challenge_full_name = f"{account_name}/{challenge_name}"
            db_challenge = DbChallenge.objects.get(fullName=challenge_full_name)  # noqa: E501
        except DoesNotExist:
            status = 400
            res = Error(f"The challenge {challenge_full_name} was not found", status)  # noqa: E501
            return res, status

        challenge_id = db_challenge.to_dict().get("id")
        db_starred_challenges = DbStarredChallenge.objects(challengeId=challenge_id).skip(offset).limit(limit)  # noqa: E501
        stargazer_ids = [d.to_dict().get("userId") for d in db_starred_challenges]  # noqa: E501
        db_stargazers = DbUser.objects(id__in=stargazer_ids)
        stargazers = [User.from_dict(d.to_dict()) for d in db_stargazers]

        next_ = ""
        if len(stargazers) == limit:
            next_ = "%s/challenges/%s/%s/stargazers?limit=%s&offset=%s" % \
                (config.server_api_url, account_name, challenge_name, limit, offset + limit)  # noqa: E501

        total = db_starred_challenges.count()
        res = PageOfUsers(
            offset=offset,
            limit=limit,
            paging={
                "next": next_
            },
            total_results=total,
            users=stargazers)
        status = 200
    except TypeError:  # TODO: may need include different exceptions for 400
        status = 400
        res = Error("Bad request", status)
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def list_challenge_topics(account_name, challenge_name):  # noqa: E501
    """List stargazers

    Lists the challenge topics. # noqa: E501

    :param account_name: The name of the account that owns the challenge
    :type account_name: str
    :param challenge_name: The name of the challenge
    :type challenge_name: str

    :rtype: ArrayOfTopics
    """
    try:
        account = DbAccount.objects.get(login=account_name)
        account_id = account.to_dict().get("id")
        db_challenge = DbChallenge.objects.get(ownerId=account_id, name=challenge_name)  # noqa: E501
        res = ArrayOfTopics(topics=db_challenge.to_dict().get("topics"))
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def list_challenges(limit=None, offset=None, sort=None, direction=None, search_terms=None, topics=None, status=None, platform_ids=None, start_date_range=None):  # noqa: E501
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
    :param topics: Array of topics used to filter the results
    :type topics: List[str]
    :param status: Array of challenge status used to filter the results
    :type status: list | bytes
    :param platform_ids: Array of challenge platform ids used to filter the results
    :type platform_ids: List[str]
    :param start_date_range: Return challenges that start during the date range specified
    :type start_date_range: dict | bytes

    :rtype: PageOfChallenges
    """
    try:
        start_date_start = None
        start_date_end = None
        if start_date_range is not None and 'start' in start_date_range:
            start_date_start = datetime.datetime.strptime(start_date_range['start'], '%Y-%m-%d')  # noqa: E501
        if start_date_range is not None and 'end' in start_date_range:
            start_date_end = datetime.datetime.strptime(start_date_range['end'], '%Y-%m-%d')  # noqa: E501

        status_q = Q(status__in=status) \
            if status is not None else Q()
        # tag_ids_q = Q(tagIds__in=tag_ids) \
        #     if tag_ids is not None and len(tag_ids) > 0 else Q()
        platform_id_q = Q(platformId__in=platform_ids) \
            if platform_ids is not None and len(platform_ids) > 0 else Q()
        startDate_start_q = Q(startDate__gte=start_date_start) \
            if start_date_start is not None else Q()
        startDate_end_q = Q(startDate__lte=start_date_end) \
            if start_date_end is not None else Q()

        db_challenges = DbChallenge.objects(status_q & platform_id_q & startDate_start_q & startDate_end_q)  # noqa: E501
        if search_terms is not None:
            db_challenges = db_challenges.search_text(search_terms)

        if sort is not None:
            order_by = ('-' if direction == 'desc' else '') + sort
            db_challenges = db_challenges.order_by(order_by)

        db_challenges = db_challenges.skip(offset).limit(limit)

        challenges = [Challenge.from_dict(d.to_dict()) for d in db_challenges]
        next_ = ""
        if len(challenges) == limit:
            next_ = "%s/challenges?limit=%s&offset=%s" % \
                (config.server_api_url, limit, offset + limit)

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
    except TypeError:  # TODO: may need include different exceptions for 400
        status = 400
        res = Error("Bad request", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


# def create_challenge_readme(account_name, challenge_name):  # noqa: E501
#     """Create a challenge README

#     Create a challenge README # noqa: E501

#     :param account_name: The name of the account that owns the challenge
#     :type account_name: str
#     :param challenge_name: The name of the challenge
#     :type challenge_name: str

#     :rtype: ChallengeReadmeCreateResponse
#     """
#     if connexion.request.is_json:
#         try:
#             try:
#                 challenge_full_name = f"{account_name}/{challenge_name}"
#                 db_challenge = DbChallenge.objects.get(fullName=challenge_full_name)  # noqa: E501
#             except DoesNotExist:
#                 status = 400
#                 res = Error(f"The challenge {challenge_full_name} was not found", status)  # noqa: E501
#                 return res, status

#             challenge_id = db_challenge.to_dict().get("id")
#             challenge_readme_create_request = ChallengeReadmeCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501

#             readme = DbChallengeReadme(
#                 text=challenge_readme_create_request.text,
#                 challengeId=challenge_id
#             ).save()

#             readme_id = readme.to_dict().get("id")
#             res = ChallengeReadmeCreateResponse(id=readme_id)
#             status = 201
#         except NotUniqueError as error:
#             status = 409
#             res = Error("Conflict", status, str(error))
#         except Exception as error:
#             status = 500
#             res = Error("Internal error", status, str(error))
#     else:
#         status = 400
#         res = Error("Bad request", status, "Missing body")
#     return res, status


def get_challenge_readme(account_name, challenge_name):  # noqa: E501
    """Get a challenge README

    Returns the challenge README specified # noqa: E501

    :param account_name: The name of the account that owns the challenge
    :type account_name: str
    :param challenge_name: The name of the challenge
    :type challenge_name: str

    :rtype: ChallengeReadme
    """
    try:
        try:
            challenge_full_name = f"{account_name}/{challenge_name}"
            db_challenge = DbChallenge.objects.get(fullName=challenge_full_name)  # noqa: E501
        except DoesNotExist:
            status = 400
            res = Error(f"The challenge {challenge_full_name} was not found", status)  # noqa: E501
            return res, status

        challenge_id = db_challenge.to_dict().get("id")
        db_readme = DbChallengeReadme.objects.get(challengeId=challenge_id)
        res = ChallengeReadme.from_dict(db_readme.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def update_challenge_readme(account_name, challenge_name):  # noqa: E501
    """Update a challenge README

    Update a challenge README # noqa: E501

    :param account_name: The name of the account that owns the challenge
    :type account_name: str
    :param challenge_name: The name of the challenge
    :type challenge_name: str

    :rtype: object
    """
    if connexion.request.is_json:
        try:
            challenge_readme_update_request = ChallengeReadmeUpdateRequest.from_dict(connexion.request.get_json())  # noqa: E501

            try:
                challenge_full_name = f"{account_name}/{challenge_name}"
                db_challenge = DbChallenge.objects.get(fullName=challenge_full_name)  # noqa: E501
            except DoesNotExist:
                status = 400
                res = Error(f"The challenge {challenge_full_name} was not found", status)  # noqa: E501
                return res, status

            challenge_id = db_challenge.to_dict().get("id")
            db_readme = DbChallengeReadme.objects.get(challengeId=challenge_id)
            db_readme.text = challenge_readme_update_request.text
            db_readme.save()

            res = {}
            status = 200
        except NotUniqueError as error:
            status = 409
            res = Error("Conflict", status, str(error))
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))
    else:
        status = 400
        res = Error("Bad request", status, "Missing body")
    return res, status


# def delete_challenge_readme(account_name, challenge_name):  # noqa: E501
#     """Delete a challenge README

#     Deletes the challenge README specified # noqa: E501

#     :param account_name: The name of the account that owns the challenge
#     :type account_name: str
#     :param challenge_name: The name of the challenge
#     :type challenge_name: str

#     :rtype: object
#     """
#     try:
#         try:
#             challenge_full_name = f"{account_name}/{challenge_name}"
#             db_challenge = DbChallenge.objects.get(fullName=challenge_full_name)  # noqa: E501
#         except DoesNotExist:
#             status = 400
#             res = Error(f"The challenge {challenge_full_name} was not found", status)  # noqa: E501
#             return res, status

#         challenge_id = db_challenge.to_dict().get("id")
#         DbChallengeReadme.objects.get(challengeId=challenge_id).delete()
#         res = {}
#         status = 200
#     except DoesNotExist:
#         status = 404
#         res = Error("The specified resource was not found", status)
#     except Exception as error:
#         status = 500
#         res = Error("Internal error", status, str(error))
#     return res, status

def create_challenge_organizer(account_name, challenge_name):  # noqa: E501
    """Create a challenge organizer

    Create a challenge organizer # noqa: E501

    :param account_name: The name of the account that owns the challenge
    :type account_name: str
    :param challenge_name: The name of the challenge
    :type challenge_name: str

    :rtype: ChallengeOrganizerCreateResponse
    """
    if connexion.request.is_json:
        try:
            try:
                challenge_full_name = f"{account_name}/{challenge_name}"
                print(f"challenge: {challenge_full_name}")
                db_challenge = DbChallenge.objects.get(fullName=challenge_full_name)  # noqa: E501
            except DoesNotExist:
                status = 400
                res = Error(f"The challenge {challenge_full_name} was not found", status)  # noqa: E501
                return res, status

            organizer_create_request = ChallengeOrganizerCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501
            organizer = DbChallengeOrganizer(
                name=organizer_create_request.name,
                login=organizer_create_request.login,  # TODO check that login exists  # noqa: E501
                roles=organizer_create_request.roles,
                challengeId=db_challenge.id
            ).save()
            organizer_id = organizer.to_dict().get("id")

            res = ChallengeOrganizerCreateResponse(id=organizer_id)
            status = 201
        except NotUniqueError as error:
            status = 409
            res = Error("Conflict", status, str(error))
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))
    else:
        status = 400
        res = Error("Bad request", status, "Missing body")
    return res, status


def delete_challenge_organizer(account_name, challenge_name, organizer_id):  # noqa: E501
    """Delete a challenge organizer

    Deletes the challenge organizer specified # noqa: E501

    :param account_name: The name of the account that owns the challenge
    :type account_name: str
    :param challenge_name: The name of the challenge
    :type challenge_name: str
    :param organizer_id: The identifier of the challenge organizer
    :type organizer_id: str

    :rtype: object
    """
    return 'do some magic!'


def list_challenge_organizers(account_name, challenge_name):  # noqa: E501
    """List organizers

    Lists the organizers of the challenge. # noqa: E501

    :param account_name: The name of the account that owns the challenge
    :type account_name: str
    :param challenge_name: The name of the challenge
    :type challenge_name: str

    :rtype: ChallengeOrganizerList
    """
    try:
        try:
            challenge_full_name = f"{account_name}/{challenge_name}"
            db_challenge = DbChallenge.objects.get(fullName=challenge_full_name)  # noqa: E501
        except DoesNotExist:
            status = 400
            res = Error(f"The challenge {challenge_full_name} was not found", status)  # noqa: E501
            return res, status

        challenge_id = db_challenge.to_dict().get("id")
        db_organizers = DbChallengeOrganizer.objects(challengeId=challenge_id)  # noqa: E501
        organizers = [ChallengeOrganizer.from_dict(d.to_dict()) for d in db_organizers]  # noqa: E501
        print(organizers)
        res = ChallengeOrganizerList(challenge_organizers=organizers)
        status = 200
    except TypeError:  # TODO: may need include different exceptions for 400
        status = 400
        res = Error("Bad request", status)
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status
