import connexion
import six

from openapi_server.models.challenge import Challenge  # noqa: E501
from openapi_server import util


def challenges_create(challenge):  # noqa: E501
    """Adds a challenge

    This can only be done by a Challenge Organizer # noqa: E501

    :param challenge: 
    :type challenge: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        challenge = Challenge.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def challenges_delete(id):  # noqa: E501
    """Removes a challenge

    Removes the challenge of the given ID  This action can only be done by a Challenge Organizer.  # noqa: E501

    :param id: challenge ID
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def challenges_read(id):  # noqa: E501
    """Lists one challenge

    Returns the challenge for a given ID # noqa: E501

    :param id: challenge ID
    :type id: str

    :rtype: Challenge
    """
    return 'do some magic!'


def challenges_read_all():  # noqa: E501
    """Lists all challenges

     # noqa: E501


    :rtype: List[Challenge]
    """
    return 'do some magic!'


def challenges_update(id):  # noqa: E501
    """Updates selected details of a challenge

    Updates and/or adds one or more details of the given challenge ID.  This action can only be done by a Challenge Organizer.  # noqa: E501

    :param id: challenge ID
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def challenges_update_all(id, challenge):  # noqa: E501
    """Updates all details of a challenge

    Updates all details of the given challenge ID.  This action can only be done by a Challenge Organizer.  # noqa: E501

    :param id: challenge ID
    :type id: str
    :param challenge: 
    :type challenge: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        challenge = Challenge.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
