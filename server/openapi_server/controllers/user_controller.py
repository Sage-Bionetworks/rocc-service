import connexion

from openapi_server.models.user import User  # noqa: E501


def get_user_by_name(username, pretty_print=None, with_email=None):  # noqa: E501
    """Get user by user name

    Some description of the operation. You can use &#x60;markdown&#x60; here.  # noqa: E501

    :param username: The name that needs to be fetched
    :type username: str
    :param pretty_print: Pretty print response
    :type pretty_print: bool
    :param with_email: Filter users without email
    :type with_email: bool

    :rtype: User
    """
    return 'do some magic!'


def update_user(username, user, pretty_print=None):  # noqa: E501
    """Updated user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name that needs to be updated
    :type username: str
    :param user: Updated user object
    :type user: dict | bytes
    :param pretty_print: Pretty print response
    :type pretty_print: bool

    :rtype: None
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501

    print(f"user: {user}")

    return 'do some magic!'
