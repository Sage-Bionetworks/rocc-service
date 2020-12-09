import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError
# import six

from openapi_server.config import Config
from openapi_server.dbmodels.challenge import Challenge as DbChallenge
from openapi_server.models.challenge import Challenge
from openapi_server.models.error import Error
from openapi_server.models.page_of_challenges import PageOfChallenges
# from openapi_server import util


def create_challenge(challenge):
    """Add a challenge

    Adds a challenge

    :param challenge:
    :type challenge: dict | bytes

    :rtype: Challenge
    """
    res = None
    status = None
    if connexion.request.is_json:
        try:
            challenge = Challenge.from_dict(connexion.request.get_json())
            db_challenge = DbChallenge(
                name=challenge.name,
                startDate=challenge.start_date,
                endDate=challenge.end_date,
                url=challenge.url,
                status=challenge.status,
                tags=challenge.tags,
                grant=challenge.grant,
                organizers=challenge.organizers
            ).save()
            status = 200
            res = Challenge.from_dict(db_challenge.to_dict())
        except NotUniqueError as error:
            status = 409
            res = Error("Conflict", status, str(error))
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))
    return res, status


def delete_challenge(id):
    """Delete a challenge

    Deletes the challenge specified

    :param id: The ID of the challenge
    :type id: str

    :rtype: Challenge
    """
    return 'do some magic!'


def get_challenge(id):
    """Get a challenge

    Returns the challenge specified

    :param id: The ID of the challenge
    :type id: str

    :rtype: Challenge
    """
    return 'do some magic!'


def list_challenges(limit=None, offset=None):
    """List all the challenges

    Returns all the challenges

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfChallenges
    """
    try:
        db_challenges = DbChallenge.objects().skip(offset).limit(limit)
        challenges = [Challenge.from_dict(c.to_dict()) for c in db_challenges]
        next_ = ""
        if len(challenges) == limit:
            next_ = '{api_url}/challenges?limit={limit}&offset={offset}'.format(  # noqa: E501
                api_url=Config().server_api_url,
                limit=limit,
                offset=offset + limit
            )
        res = PageOfChallenges(
            offset=offset,
            limit=limit,
            links={
                "next": next_
            },
            challenges=challenges
        )
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status
