import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.local_auth_request import LocalAuthRequest  # noqa: E501
from openapi_server import util


def auth_local(local_auth_request):  # noqa: E501
    """Authentify a local account

    Authentify a local account with the specified credential # noqa: E501

    :param local_auth_request: 
    :type local_auth_request: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        local_auth_request = LocalAuthRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
