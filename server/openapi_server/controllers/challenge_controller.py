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
            res = Challenge.from_dict(db_challenge.to_dict())
            status = 200
        except NotUniqueError as error:
            res = Error("Conflict", status, str(error))
            status = 409
        except Exception as error:
            res = Error("Internal error", status, str(error))
            status = 500
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
    return 'do some magic!'
