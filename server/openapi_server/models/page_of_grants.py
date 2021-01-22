# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.grant import Grant
from openapi_server.models.response_page_metadata_links import ResponsePageMetadataLinks  # noqa: E501
from openapi_server import util


class PageOfGrants(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, offset=None, limit=None, links=None, total_results=None, grants=None):  # noqa: E501
        """PageOfGrants - a model defined in OpenAPI

        :param offset: The offset of this PageOfGrants.  # noqa: E501
        :type offset: int
        :param limit: The limit of this PageOfGrants.  # noqa: E501
        :type limit: int
        :param links: The links of this PageOfGrants.  # noqa: E501
        :type links: ResponsePageMetadataLinks
        :param total_results: The total_results of this PageOfGrants.  # noqa: E501
        :type total_results: int
        :param grants: The grants of this PageOfGrants.  # noqa: E501
        :type grants: List[Grant]
        """
        self.openapi_types = {
            'offset': int,
            'limit': int,
            'links': ResponsePageMetadataLinks,
            'total_results': int,
            'grants': List[Grant]
        }

        self.attribute_map = {
            'offset': 'offset',
            'limit': 'limit',
            'links': 'links',
            'total_results': 'totalResults',
            'grants': 'grants'
        }

        self._offset = offset
        self._limit = limit
        self._links = links
        self._total_results = total_results
        self._grants = grants

    @classmethod
    def from_dict(cls, dikt) -> 'PageOfGrants':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PageOfGrants of this PageOfGrants.  # noqa: E501
        :rtype: PageOfGrants
        """
        return util.deserialize_model(dikt, cls)

    @property
    def offset(self):
        """Gets the offset of this PageOfGrants.

        Index of the first result that must be returned  # noqa: E501

        :return: The offset of this PageOfGrants.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PageOfGrants.

        Index of the first result that must be returned  # noqa: E501

        :param offset: The offset of this PageOfGrants.
        :type offset: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this PageOfGrants.

        Maximum number of results returned  # noqa: E501

        :return: The limit of this PageOfGrants.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PageOfGrants.

        Maximum number of results returned  # noqa: E501

        :param limit: The limit of this PageOfGrants.
        :type limit: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def links(self):
        """Gets the links of this PageOfGrants.


        :return: The links of this PageOfGrants.
        :rtype: ResponsePageMetadataLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PageOfGrants.


        :param links: The links of this PageOfGrants.
        :type links: ResponsePageMetadataLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def total_results(self):
        """Gets the total_results of this PageOfGrants.

        Total number of results in the result set  # noqa: E501

        :return: The total_results of this PageOfGrants.
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this PageOfGrants.

        Total number of results in the result set  # noqa: E501

        :param total_results: The total_results of this PageOfGrants.
        :type total_results: int
        """

        self._total_results = total_results

    @property
    def grants(self):
        """Gets the grants of this PageOfGrants.

        An array of Grants  # noqa: E501

        :return: The grants of this PageOfGrants.
        :rtype: List[Grant]
        """
        return self._grants

    @grants.setter
    def grants(self, grants):
        """Sets the grants of this PageOfGrants.

        An array of Grants  # noqa: E501

        :param grants: The grants of this PageOfGrants.
        :type grants: List[Grant]
        """

        self._grants = grants
