# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util


class UserCreateResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, username=None, role='user'):
        """UserCreateResponse - a model defined in OpenAPI

        :param username: The username of this UserCreateResponse.  # noqa: E501
        :type username: str
        :param role: The role of this UserCreateResponse.  # noqa: E501
        :type role: str
        """
        self.openapi_types = {
            'username': str,
            'role': str
        }

        self.attribute_map = {
            'username': 'username',
            'role': 'role'
        }

        self._username = username
        self._role = role

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
    def username(self):
        """Gets the username of this UserCreateResponse.

        The username of the user  # noqa: E501

        :return: The username of this UserCreateResponse.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserCreateResponse.

        The username of the user  # noqa: E501

        :param username: The username of this UserCreateResponse.
        :type username: str
        """
        if username is not None and len(username) > 25:
            raise ValueError("Invalid value for `username`, length must be less than or equal to `25`")  # noqa: E501
        if username is not None and len(username) < 3:
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `3`")  # noqa: E501
        if username is not None and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', username):  # noqa: E501
            raise ValueError("Invalid value for `username`, must be a follow pattern or equal to `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501

        self._username = username

    @property
    def role(self):
        """Gets the role of this UserCreateResponse.

        The role of the user  # noqa: E501

        :return: The role of this UserCreateResponse.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UserCreateResponse.

        The role of the user  # noqa: E501

        :param role: The role of this UserCreateResponse.
        :type role: str
        """
        allowed_values = ["user", "admin"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"
                .format(role, allowed_values)
            )

        self._role = role