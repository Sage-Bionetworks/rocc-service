import connexion
import six

from openapi_server.models.challenge import Challenge  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_challenges import PageOfChallenges  # noqa: E501
from openapi_server import util


def create_challenge(challenge):  # noqa: E501
    """Add a challenge

    Adds a challenge # noqa: E501

    :param challenge: 
    :type challenge: dict | bytes

    :rtype: Challenge
    """
    if connexion.request.is_json:
        challenge = Challenge.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_challenge(challenge_id):  # noqa: E501
    """Delete a challenge

    Deletes the challenge specified # noqa: E501

    :param challenge_id: The ID of the challenge
    :type challenge_id: str

    :rtype: Challenge
    """
    return 'do some magic!'


def get_challenge(challenge_id):  # noqa: E501
    """Get a challenge

    Returns the challenge specified # noqa: E501

    :param challenge_id: The ID of the challenge
    :type challenge_id: str

    :rtype: Challenge
    """
    return 'do some magic!'


def list_challenges(limit=None, offset=None):  # noqa: E501
    """List all the challenges

    Returns all the challenges # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfChallenges
    """
    return 'do some magic!'
