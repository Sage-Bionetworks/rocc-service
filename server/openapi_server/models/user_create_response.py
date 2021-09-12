# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class UserCreateResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, token=None):  # noqa: E501
        """UserCreateResponse - a model defined in OpenAPI

        :param id: The id of this UserCreateResponse.  # noqa: E501
        :type id: str
        :param token: The token of this UserCreateResponse.  # noqa: E501
        :type token: str
        """
        self.openapi_types = {
            'id': str,
            'token': str
        }

        self.attribute_map = {
            'id': 'id',
            'token': 'token'
        }

        self._id = id
        self._token = token

    @classmethod
    def from_dict(cls, dikt) -> 'UserCreateResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserCreateResponse of this UserCreateResponse.  # noqa: E501
        :rtype: UserCreateResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this UserCreateResponse.

        The unique identifier of an account  # noqa: E501

        :return: The id of this UserCreateResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserCreateResponse.

        The unique identifier of an account  # noqa: E501

        :param id: The id of this UserCreateResponse.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def token(self):
        """Gets the token of this UserCreateResponse.


        :return: The token of this UserCreateResponse.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UserCreateResponse.


        :param token: The token of this UserCreateResponse.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token
