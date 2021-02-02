import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError

from openapi_server.dbmodels.user import User as DbUser
from openapi_server.dbmodels.organization import Organization as DbOrganization  # noqa: E501
from openapi_server.models.error import Error
from openapi_server.models.page_of_users import PageOfUsers
from openapi_server.models.user import User
from openapi_server.models.user_create_response import UserCreateResponse
from openapi_server.config import Config


def create_user(username):
    """Create a user

    Create a user with the specified username # noqa: E501

    :param username: The username of the user that is being created
    :type username: str

    :rtype: UserCreateResponse
    """
    res = None
    status = None
    try:
        if connexion.request.is_json:
            user = User.from_dict(connexion.request.get_json())

            # Check that the organization specified exists
            for org_id in user.organizations:
                try:
                    DbOrganization.objects.get(organizationId=org_id)
                except DoesNotExist:
                    status = 404
                    res = Error(
                        f"The organization, {org_id}, was not found",
                        status)
                    return res, status

            # Create the user
            try:
                DbUser(
                    username=username,
                    # password=user.password,
                    firstName=user.first_name,
                    lastName=user.last_name,
                    email=user.email,
                    organizations=user.organizations
                ).save(force_insert=True)
                res = UserCreateResponse(username=username)
                status = 201
            except NotUniqueError as error:
                status = 409
                res = Error("Conflict", status, str(error))
        else:
            status = 400
            res = Error("Bad request", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def delete_user(username):
    """Delete a user

    Deletes the user specified # noqa: E501

    :param username: The username of the user
    :type username: str

    :rtype: object
    """
    res = None
    status = None
    try:
        DbUser.objects.get(username=username).delete()
        res = {}
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def get_user(username):
    """Get a user

    Returns the user specified # noqa: E501

    :param username: The username of the user
    :type username: str

    :rtype: User
    """
    res = None
    status = None
    try:
        db_user = DbUser.objects.get(username=username)
        res = User.from_dict(db_user.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def list_users(limit=None, offset=None):
    """Get all users

    Returns the users # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfUsers
    """
    res = None
    status = None
    try:
        db_users = DbUser.objects.skip(offset).limit(limit)
        users = [User.from_dict(d.to_dict()) for d in db_users]
        next_ = ""
        if len(users) == limit:
            next_ = "%s/orgs?limit=%s&offset=%s" % \
                (Config().server_api_url, limit, offset + limit)
        res = PageOfUsers(
            offset=offset,
            limit=limit,
            links={
                "next": next_
            },
            total_results=len(users),
            users=users)
        status = 200
    except TypeError:  # TODO: may need different exception
        status = 400
        res = Error("Bad request", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status
