# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ChallengePlatformAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created_at=None, updated_at=None):  # noqa: E501
        """ChallengePlatformAllOf - a model defined in OpenAPI

        :param created_at: The created_at of this ChallengePlatformAllOf.  # noqa: E501
        :type created_at: datetime
        :param updated_at: The updated_at of this ChallengePlatformAllOf.  # noqa: E501
        :type updated_at: datetime
        """
        self.openapi_types = {
            'created_at': datetime,
            'updated_at': datetime
        }

        self.attribute_map = {
            'created_at': 'createdAt',
            'updated_at': 'updatedAt'
        }

        self._created_at = created_at
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt) -> 'ChallengePlatformAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChallengePlatform_allOf of this ChallengePlatformAllOf.  # noqa: E501
        :rtype: ChallengePlatformAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created_at(self):
        """Gets the created_at of this ChallengePlatformAllOf.

        When this challenge platform has been created  # noqa: E501

        :return: The created_at of this ChallengePlatformAllOf.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ChallengePlatformAllOf.

        When this challenge platform has been created  # noqa: E501

        :param created_at: The created_at of this ChallengePlatformAllOf.
        :type created_at: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ChallengePlatformAllOf.

        When this challenge platform has last been updated  # noqa: E501

        :return: The updated_at of this ChallengePlatformAllOf.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ChallengePlatformAllOf.

        When this challenge platform has last been updated  # noqa: E501

        :param updated_at: The updated_at of this ChallengePlatformAllOf.
        :type updated_at: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at
