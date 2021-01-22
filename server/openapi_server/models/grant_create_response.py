# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class GrantCreateResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, grant_id=None):  # noqa: E501
        """GrantCreateResponse - a model defined in OpenAPI

        :param grant_id: The grant_id of this GrantCreateResponse.  # noqa: E501
        :type grant_id: str
        """
        self.openapi_types = {
            'grant_id': str
        }

        self.attribute_map = {
            'grant_id': 'grantId'
        }

        self._grant_id = grant_id

    @classmethod
    def from_dict(cls, dikt) -> 'GrantCreateResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GrantCreateResponse of this GrantCreateResponse.  # noqa: E501
        :rtype: GrantCreateResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def grant_id(self):
        """Gets the grant_id of this GrantCreateResponse.

        The ID of the grant  # noqa: E501

        :return: The grant_id of this GrantCreateResponse.
        :rtype: str
        """
        return self._grant_id

    @grant_id.setter
    def grant_id(self, grant_id):
        """Sets the grant_id of this GrantCreateResponse.

        The ID of the grant  # noqa: E501

        :param grant_id: The grant_id of this GrantCreateResponse.
        :type grant_id: str
        """

        self._grant_id = grant_id
