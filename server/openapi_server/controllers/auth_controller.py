import connexion
from mongoengine.errors import DoesNotExist
from werkzeug.security import check_password_hash

from openapi_server.dbmodels.user import User as DbUser  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.local_auth_request import LocalAuthRequest  # noqa: E501
# from openapi_server import util


def auth_local():  # noqa: E501
    """Authentify a local account

    Authentify a local account with the specified credential # noqa: E501

    :rtype: object
    """
    if connexion.request.is_json:
        try:
            local_auth_request = LocalAuthRequest.from_dict(connexion.request.get_json())  # noqa: E501
            db_user = DbUser.objects.get(login=local_auth_request.login)
            if check_password_hash(db_user.passwordHash, local_auth_request.password):  # noqa: E501
                res = {}
                status = 200
            else:
                res = Error("Invalid login or password")
                status = 401
        except DoesNotExist:
            status = 404
            res = Error("The specified resource was not found", status)
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))
    else:
        status = 400
        res = Error("Bad request", status, "Missing body")
    return res, status
