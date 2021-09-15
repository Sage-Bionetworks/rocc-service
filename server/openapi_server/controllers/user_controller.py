import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError

from openapi_server.dbmodels.user import User as DbUser
from openapi_server.models.error import Error
from openapi_server.models.page_of_users import PageOfUsers
from openapi_server.models.user import User
from openapi_server.models.user_create_response import UserCreateResponse
from openapi_server.models.user_create_request import UserCreateRequest
from openapi_server.config import config


def create_user():  # noqa: E501
    """Create a user

    Create a user with the specified account name # noqa: E501

    :rtype: UserCreateResponse
    """
    if connexion.request.is_json:
        try:
            user_create_request = UserCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501
            user = DbUser(
                login=user_create_request.login,
                email=user_create_request.email,
                passwordHash=DbUser.generate_password_hash(user_create_request.password),  # noqa: E501
                name=user_create_request.name,
                avatarUrl=user_create_request.avatar_url,
                type="User"  # TODO: Use enum value
            ).save()
            user_id = user.to_dict().get("id")
            res = UserCreateResponse(id=user_id)
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


def delete_all_users():  # noqa: E501
    """Delete all users

    Delete all users # noqa: E501

    :rtype: object
    """
    try:
        DbUser.objects.delete()
        res = {}
        status = 200
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def delete_user(user_id):  # noqa: E501
    """Delete a user

    Deletes the user specified # noqa: E501

    :param user_id: The unique identifier of the user, either the user account ID or login
    :type user_id: str

    :rtype: object
    """
    try:
        DbUser.objects.get(id=user_id).delete()
        res = {}
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def get_user(user_id):  # noqa: E501
    """Get a user

    Returns the user specified # noqa: E501

    :param user_id: The unique identifier of the user, either the user account ID or login
    :type user_id: str

    :rtype: User
    """
    try:
        db_user = DbUser.objects.get(id=user_id)
        res = User.from_dict(db_user.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def get_user_starred_challenges(user_id):  # noqa: E501
    """List repositories starred by a user

    Lists repositories a user has starred. # noqa: E501

    :param user_id: The unique identifier of the user, either the user account ID or login
    :type user_id: str

    :rtype: PageOfChallenges
    """
    return 'do some magic!'


def is_starred_challenge(account_name, challenge_name):  # noqa: E501
    """Check if a repository is starred by the authenticated user

    Check if a repository is starred by the authenticated user # noqa: E501

    :param account_name: The name of the account that owns the challenge
    :type account_name: str
    :param challenge_name: The name of the challenge
    :type challenge_name: str

    :rtype: object
    """
    return 'do some magic!'


def list_starred_challenges():  # noqa: E501
    """List challenges starred by the authenticated user

    Lists repositories the authenticated user has starred. # noqa: E501


    :rtype: PageOfChallenges
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
    try:
        db_users = DbUser.objects.skip(offset).limit(limit)
        users = [User.from_dict(d.to_dict()) for d in db_users]
        next_ = ""
        if len(users) == limit:
            next_ = "%s/users?limit=%s&offset=%s" % \
                (config.server_api_url, limit, offset + limit)

        total = db_users.count()
        res = PageOfUsers(
            offset=offset,
            limit=limit,
            paging={
                "next": next_
            },
            total_results=total,
            users=users)
        status = 200
    except TypeError:  # TODO: may need include different exceptions for 400
        status = 400
        res = Error("Bad request", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def star_challenge(account_name, challenge_name):  # noqa: E501
    """Star a repository for the authenticated user

    Star a repository for the authenticated user # noqa: E501

    :param account_name: The name of the account that owns the challenge
    :type account_name: str
    :param challenge_name: The name of the challenge
    :type challenge_name: str

    :rtype: object
    """
    return 'do some magic!'


def get_authenticated_user(token_info):  # noqa: E501
    """Get the authenticated user

    Get the authenticated user # noqa: E501

    :rtype: User
    """
    try:
        user_id = token_info['sub']
        db_user = DbUser.objects.get(id=user_id)
        res = User.from_dict(db_user.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status
