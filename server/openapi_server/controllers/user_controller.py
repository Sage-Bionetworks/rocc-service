import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError
from werkzeug.security import generate_password_hash
import jwt
import datetime

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

    :rtype: TokenResponse
    """
    if connexion.request.is_json:
        try:
            user_create_request = UserCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501
            user = DbUser(
                login=user_create_request.login,
                email=user_create_request.email,
                passwordHash=generate_password_hash(user_create_request.password),  # noqa: E501
                name=user_create_request.name,
                avatarUrl=user_create_request.avatar_url,
                type="User"  # TODO: Use enum value
            ).save()

            # Returns a JWT (RFC 7519) signed by the app secret.
            user_id = user.to_dict().get("id")
            payload = {
                "sub": user_id,
                "iat": datetime.datetime.utcnow(),
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=30)  # noqa: E501
            }
            token = jwt.encode(payload, config.secret_key, algorithm="HS256")
            res = UserCreateResponse(id=user_id, token=token)
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
