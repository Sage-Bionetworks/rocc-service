import connexion
import six

from openapi_server.models.challenge import Challenge  # noqa: E501
from openapi_server import util


def challenges_read(id):  # noqa: E501
    """Get a challenge by ID

    Returns the challenge for a given ID # noqa: E501

    :param id: The ID of the challenge to fetch
    :type id: str

    :rtype: Challenge
    """
    return 'do some magic!'


def challenges_update(id, challenge):  # noqa: E501
    """Update a challenge by ID

    This can only be done by the logged in user. # noqa: E501

    :param id: Updates the challenge for a given ID
    :type id: str
    :param challenge: Updated challenge
    :type challenge: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        challenge = Challenge.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def notes_read_all():  # noqa: E501
    """Get all challenges

    Returns the challenges # noqa: E501


    :rtype: List[Challenge]
    """
    return 'do some magic!'
