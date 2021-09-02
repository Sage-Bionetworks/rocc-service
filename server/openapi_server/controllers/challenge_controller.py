import connexion
import six

from openapi_server.models.challenge import Challenge  # noqa: E501
from openapi_server.models.challenge_create_request import ChallengeCreateRequest  # noqa: E501
from openapi_server.models.challenge_create_response import ChallengeCreateResponse  # noqa: E501
from openapi_server.models.challenge_status import ChallengeStatus  # noqa: E501
from openapi_server.models.date_range import DateRange  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_challenges import PageOfChallenges  # noqa: E501
from openapi_server import util


def create_challenge(challenge_create_request):  # noqa: E501
    """Add a challenge

    Adds a challenge # noqa: E501

    :param challenge_create_request: 
    :type challenge_create_request: dict | bytes

    :rtype: ChallengeCreateResponse
    """
    if connexion.request.is_json:
        challenge_create_request = ChallengeCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_all_challenges():  # noqa: E501
    """Delete all challenges

    Delete all challenges # noqa: E501


    :rtype: object
    """
    return 'do some magic!'


def delete_challenge(account_name, challenge_name):  # noqa: E501
    """Delete a challenge

    Deletes the challenge specified # noqa: E501

    :param account_name: The name of the account that owns the challenge
    :type account_name: str
    :param challenge_name: The name of the challenge
    :type challenge_name: str

    :rtype: object
    """
    return 'do some magic!'


def get_challenge(account_name, challenge_name):  # noqa: E501
    """Get a challenge

    Returns the challenge specified # noqa: E501

    :param account_name: The name of the account that owns the challenge
    :type account_name: str
    :param challenge_name: The name of the challenge
    :type challenge_name: str

    :rtype: Challenge
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
    if connexion.request.is_json:
        status = [ChallengeStatus.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        start_date_range =  DateRange.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
