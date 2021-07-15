import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError
from mongoengine.queryset.visitor import Q

from openapi_server.dbmodels.challenge_platform import ChallengePlatform as DbChallengePlatform
from openapi_server.models.challenge_platform import ChallengePlatform  # noqa: E501
from openapi_server.models.challenge_platform_create_request import ChallengePlatformCreateRequest  # noqa: E501
from openapi_server.models.challenge_platform_create_response import ChallengePlatformCreateResponse  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_challenge_platforms import PageOfChallengePlatforms  # noqa: E501
from openapi_server.config import Config

def create_challenge_platform(challenge_platform_id):  # noqa: E501
    """Create a challenge platform

    Create a challenge platform with the specified ID # noqa: E501

    :param challenge_platform_id: The ID of the challenge platform that is being created
    :type challenge_platform_id: str

    :rtype: ChallengePlatformCreateResponse
    """
    res = None
    status = None
    if connexion.request.is_json:
        try:
            platform = ChallengePlatform.from_dict(connexion.request.get_json())
            DbChallengePlatform(
                id=challenge_platform_id,
                name=platform.name,
                url=platform.url
            ).save(force_insert=True)
            res = ChallengePlatformCreateResponse(id=challenge_platform_id)
            status = 201
        except NotUniqueError as error:
            status = 409
            res = Error("Conflict", status, str(error))
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))
    else:
        status = 400
        res = Error("Bad request", status)
    return res, status


def delete_all_challenge_platforms():  # noqa: E501
    """Delete all challenge platforms

    Delete all challenge platforms # noqa: E501


    :rtype: object
    """
    return 'do some magic!'


def delete_challenge_platform(challenge_platform_id):  # noqa: E501
    """Delete a challenge platform

    Deletes the challenge platform specified # noqa: E501

    :param challenge_platform_id: The ID of the challenge platform
    :type challenge_platform_id: str

    :rtype: object
    """
    return 'do some magic!'


def get_challenge_platform(challenge_platform_id):  # noqa: E501
    """Get a challenge platform

    Returns the challenge platform specified # noqa: E501

    :param challenge_platform_id: The ID of the challenge platform
    :type challenge_platform_id: str

    :rtype: ChallengePlatform
    """
    return 'do some magic!'


def list_challenge_platforms(limit=None, offset=None):  # noqa: E501
    """Get all challenge platforms

    Returns the challenge platforms # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfChallengePlatforms
    """
    return 'do some magic!'
