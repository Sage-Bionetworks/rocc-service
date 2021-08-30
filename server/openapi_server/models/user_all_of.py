# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class UserAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, avatar_url=None, created_at=None, updated_at=None, type=None):  # noqa: E501
        """UserAllOf - a model defined in OpenAPI

        :param name: The name of this UserAllOf.  # noqa: E501
        :type name: str
        :param avatar_url: The avatar_url of this UserAllOf.  # noqa: E501
        :type avatar_url: str
        :param created_at: The created_at of this UserAllOf.  # noqa: E501
        :type created_at: datetime
        :param updated_at: The updated_at of this UserAllOf.  # noqa: E501
        :type updated_at: datetime
        :param type: The type of this UserAllOf.  # noqa: E501
        :type type: str
        """
        self.openapi_types = {
            'name': str,
            'avatar_url': str,
            'created_at': datetime,
            'updated_at': datetime,
            'type': str
        }

        self.attribute_map = {
            'name': 'name',
            'avatar_url': 'avatarUrl',
            'created_at': 'createdAt',
            'updated_at': 'updatedAt',
            'type': 'type'
        }

        self._name = name
        self._avatar_url = avatar_url
        self._created_at = created_at
        self._updated_at = updated_at
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'UserAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User_allOf of this UserAllOf.  # noqa: E501
        :rtype: UserAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this UserAllOf.


        :return: The name of this UserAllOf.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserAllOf.


        :param name: The name of this UserAllOf.
        :type name: str
        """

        self._name = name

    @property
    def avatar_url(self):
        """Gets the avatar_url of this UserAllOf.


        :return: The avatar_url of this UserAllOf.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this UserAllOf.


        :param avatar_url: The avatar_url of this UserAllOf.
        :type avatar_url: str
        """

        self._avatar_url = avatar_url

    @property
    def created_at(self):
        """Gets the created_at of this UserAllOf.


        :return: The created_at of this UserAllOf.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserAllOf.


        :param created_at: The created_at of this UserAllOf.
        :type created_at: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this UserAllOf.


        :return: The updated_at of this UserAllOf.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UserAllOf.


        :param updated_at: The updated_at of this UserAllOf.
        :type updated_at: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def type(self):
        """Gets the type of this UserAllOf.


        :return: The type of this UserAllOf.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserAllOf.


        :param type: The type of this UserAllOf.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type
