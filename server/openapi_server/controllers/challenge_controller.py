import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError

from openapi_server.dbmodels.account import Account as DbAccount
from openapi_server.dbmodels.challenge import Challenge as DbChallenge
from openapi_server.dbmodels.challenge_platform import ChallengePlatform as DbChallengePlatform  # noqa: E501
from openapi_server.dbmodels.challenge_readme import ChallengeReadme as DbChallengeReadme  # noqa: E501
from openapi_server.models.challenge import Challenge  # noqa: E501
from openapi_server.models.challenge_create_request import ChallengeCreateRequest  # noqa: E501
from openapi_server.models.challenge_create_response import ChallengeCreateResponse  # noqa: E501
from openapi_server.models.challenge_readme import ChallengeReadme  # noqa: E501
from openapi_server.models.challenge_readme_create_request import ChallengeReadmeCreateRequest  # noqa: E501
from openapi_server.models.challenge_readme_create_response import ChallengeReadmeCreateResponse  # noqa: E501
# from openapi_server.models.challenge_status import ChallengeStatus  # noqa: E501
# from openapi_server.models.date_range import DateRange  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_challenges import PageOfChallenges  # noqa: E501
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
              doi=challenge_create_request.doi,
              fullName="%s/%s" % (account_name, challenge_create_request.name),
              ownerId=account_id
            ).save()
            challenge_id = challenge.to_dict().get("id")
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
        DbChallenge.objects.get(owner_id=account_id, name=challenge_name).delete()  # noqa: E501
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
        db_user = DbChallenge.objects.get(ownerId=account_id, name=challenge_name)  # noqa: E501
        res = Challenge.from_dict(db_user.to_dict())
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


def list_challenge_stargazers(account_name, challenge_name):  # noqa: E501
    """List stargazers
    Lists the people that have starred the repository. # noqa: E501
    :param account_name: The name of the account that owns the challenge
    :type account_name: str
    :param challenge_name: The name of the challenge
    :type challenge_name: str
    :rtype: PageOfUsers
    """
    return 'do some magic!'


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
    try:
        db_challenges = DbChallenge.objects.skip(offset).limit(limit)
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


def create_challenge_readme(account_name, challenge_name):  # noqa: E501
    """Create a challenge README

    Create a challenge README # noqa: E501

    :param account_name: The name of the account that owns the challenge
    :type account_name: str
    :param challenge_name: The name of the challenge
    :type challenge_name: str

    :rtype: ChallengeReadmeCreateResponse
    """
    if connexion.request.is_json:
        try:
            try:
                challenge_full_name = f"{account_name}/{challenge_name}"
                db_challenge = DbChallenge.objects.get(fullName=challenge_full_name)  # noqa: E501
            except DoesNotExist:
                status = 400
                res = Error(f"The challenge {challenge_full_name} was not found", status)  # noqa: E501
                return res, status

            challenge_id = db_challenge.to_dict().get("id")
            challenge_readme_create_request = ChallengeReadmeCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501

            readme = DbChallengeReadme(
                text=challenge_readme_create_request.text,
                challengeId=challenge_id
            ).save()

            readme_id = readme.to_dict().get("id")
            res = ChallengeReadmeCreateResponse(id=readme_id)
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


def delete_challenge_readme(account_name, challenge_name):  # noqa: E501
    """Delete a challenge README

    Deletes the challenge README specified # noqa: E501

    :param account_name: The name of the account that owns the challenge
    :type account_name: str
    :param challenge_name: The name of the challenge
    :type challenge_name: str

    :rtype: object
    """
    return 'do some magic!'
