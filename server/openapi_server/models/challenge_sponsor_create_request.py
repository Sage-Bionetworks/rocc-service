# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.challenge_sponsor_role import ChallengeSponsorRole
import re
from openapi_server import util

from openapi_server.models.challenge_sponsor_role import ChallengeSponsorRole  # noqa: E501
import re  # noqa: E501

class ChallengeSponsorCreateRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, login=None, roles=None):  # noqa: E501
        """ChallengeSponsorCreateRequest - a model defined in OpenAPI

        :param name: The name of this ChallengeSponsorCreateRequest.  # noqa: E501
        :type name: str
        :param login: The login of this ChallengeSponsorCreateRequest.  # noqa: E501
        :type login: str
        :param roles: The roles of this ChallengeSponsorCreateRequest.  # noqa: E501
        :type roles: List[ChallengeSponsorRole]
        """
        self.openapi_types = {
            'name': str,
            'login': str,
            'roles': List[ChallengeSponsorRole]
        }

        self.attribute_map = {
            'name': 'name',
            'login': 'login',
            'roles': 'roles'
        }

        self._name = name
        self._login = login
        self._roles = roles

    @classmethod
    def from_dict(cls, dikt) -> 'ChallengeSponsorCreateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChallengeSponsorCreateRequest of this ChallengeSponsorCreateRequest.  # noqa: E501
        :rtype: ChallengeSponsorCreateRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this ChallengeSponsorCreateRequest.


        :return: The name of this ChallengeSponsorCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChallengeSponsorCreateRequest.


        :param name: The name of this ChallengeSponsorCreateRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def login(self):
        """Gets the login of this ChallengeSponsorCreateRequest.

        The user or organization account name  # noqa: E501

        :return: The login of this ChallengeSponsorCreateRequest.
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this ChallengeSponsorCreateRequest.

        The user or organization account name  # noqa: E501

        :param login: The login of this ChallengeSponsorCreateRequest.
        :type login: str
        """
        if login is not None and len(login) > 25:
            raise ValueError("Invalid value for `login`, length must be less than or equal to `25`")  # noqa: E501
        if login is not None and len(login) < 3:
            raise ValueError("Invalid value for `login`, length must be greater than or equal to `3`")  # noqa: E501
        if login is not None and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', login):  # noqa: E501
            raise ValueError("Invalid value for `login`, must be a follow pattern or equal to `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501

        self._login = login

    @property
    def roles(self):
        """Gets the roles of this ChallengeSponsorCreateRequest.


        :return: The roles of this ChallengeSponsorCreateRequest.
        :rtype: List[ChallengeSponsorRole]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this ChallengeSponsorCreateRequest.


        :param roles: The roles of this ChallengeSponsorCreateRequest.
        :type roles: List[ChallengeSponsorRole]
        """

        self._roles = roles