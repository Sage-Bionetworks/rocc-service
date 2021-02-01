import connexion

from openapi_server.models.error import Error
from openapi_server.models.page_of_users import PageOfUsers
from openapi_server.models.user import User
from openapi_server.models.user_create_request import UserCreateRequest
from openapi_server.models.user_create_response import UserCreateResponse


def create_user(username, user_create_request=None):  # noqa: E501
    """Create a user

    Create a user with the specified username # noqa: E501

    :param username: The username of the user that is being created
    :type username: str
    :param user_create_request:
    :type user_create_request: dict | bytes

    :rtype: UserCreateResponse
    """
    if connexion.request.is_json:
        user_create_request = UserCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user(username):  # noqa: E501
    """Delete a user

    Deletes the user specified # noqa: E501

    :param username: The username of the user
    :type username: str

    :rtype: object
    """
    return 'do some magic!'


def get_user(username):  # noqa: E501
    """Get a user

    Returns the user specified # noqa: E501

    :param username: The username of the user
    :type username: str

    :rtype: User
    """
    return 'do some magic!'


def list_users(limit=None, offset=None):  # noqa: E501
    """Get all users

    Returns the users # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfUsers
    """
    return 'do some magic!'
