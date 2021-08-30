# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class UserCreateRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, login=None, email=None):  # noqa: E501
        """UserCreateRequest - a model defined in OpenAPI

        :param login: The login of this UserCreateRequest.  # noqa: E501
        :type login: str
        :param email: The email of this UserCreateRequest.  # noqa: E501
        :type email: str
        """
        self.openapi_types = {
            'login': str,
            'email': str
        }

        self.attribute_map = {
            'login': 'login',
            'email': 'email'
        }

        self._login = login
        self._email = email

    @classmethod
    def from_dict(cls, dikt) -> 'UserCreateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserCreateRequest of this UserCreateRequest.  # noqa: E501
        :rtype: UserCreateRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def login(self):
        """Gets the login of this UserCreateRequest.


        :return: The login of this UserCreateRequest.
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this UserCreateRequest.


        :param login: The login of this UserCreateRequest.
        :type login: str
        """
        if login is None:
            raise ValueError("Invalid value for `login`, must not be `None`")  # noqa: E501

        self._login = login

    @property
    def email(self):
        """Gets the email of this UserCreateRequest.

        An email address  # noqa: E501

        :return: The email of this UserCreateRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserCreateRequest.

        An email address  # noqa: E501

        :param email: The email of this UserCreateRequest.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email
