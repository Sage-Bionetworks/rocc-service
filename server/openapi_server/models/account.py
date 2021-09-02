# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class Account(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, login=None, type=None):  # noqa: E501
        """Account - a model defined in OpenAPI

        :param id: The id of this Account.  # noqa: E501
        :type id: str
        :param login: The login of this Account.  # noqa: E501
        :type login: str
        :param type: The type of this Account.  # noqa: E501
        :type type: str
        """
        self.openapi_types = {
            'id': str,
            'login': str,
            'type': str
        }

        self.attribute_map = {
            'id': 'id',
            'login': 'login',
            'type': 'type'
        }

        self._id = id
        self._login = login
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'Account':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Account of this Account.  # noqa: E501
        :rtype: Account
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Account.

        The unique identifier of an account  # noqa: E501

        :return: The id of this Account.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Account.

        The unique identifier of an account  # noqa: E501

        :param id: The id of this Account.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def login(self):
        """Gets the login of this Account.

        The user or organization account name  # noqa: E501

        :return: The login of this Account.
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this Account.

        The user or organization account name  # noqa: E501

        :param login: The login of this Account.
        :type login: str
        """
        if login is None:
            raise ValueError("Invalid value for `login`, must not be `None`")  # noqa: E501
        if login is not None and len(login) > 25:
            raise ValueError("Invalid value for `login`, length must be less than or equal to `25`")  # noqa: E501
        if login is not None and len(login) < 3:
            raise ValueError("Invalid value for `login`, length must be greater than or equal to `3`")  # noqa: E501
        if login is not None and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', login):  # noqa: E501
            raise ValueError("Invalid value for `login`, must be a follow pattern or equal to `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501

        self._login = login

    @property
    def type(self):
        """Gets the type of this Account.


        :return: The type of this Account.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Account.


        :param type: The type of this Account.
        :type type: str
        """
        allowed_values = ["User", "Organization"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
