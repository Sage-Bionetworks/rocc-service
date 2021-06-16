# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.grant import Grant
from openapi_server.models.page_of_grants_all_of import PageOfGrantsAllOf
from openapi_server.models.response_page_metadata import ResponsePageMetadata
from openapi_server.models.response_page_metadata_paging import ResponsePageMetadataPaging
from openapi_server import util

from openapi_server.models.grant import Grant  # noqa: E501
from openapi_server.models.page_of_grants_all_of import PageOfGrantsAllOf  # noqa: E501
from openapi_server.models.response_page_metadata import ResponsePageMetadata  # noqa: E501
from openapi_server.models.response_page_metadata_paging import ResponsePageMetadataPaging  # noqa: E501

class PageOfGrants(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, offset=None, limit=None, paging=None, total_results=None, grants=None):  # noqa: E501
        """PageOfGrants - a model defined in OpenAPI

        :param offset: The offset of this PageOfGrants.  # noqa: E501
        :type offset: int
        :param limit: The limit of this PageOfGrants.  # noqa: E501
        :type limit: int
        :param paging: The paging of this PageOfGrants.  # noqa: E501
        :type paging: ResponsePageMetadataPaging
        :param total_results: The total_results of this PageOfGrants.  # noqa: E501
        :type total_results: int
        :param grants: The grants of this PageOfGrants.  # noqa: E501
        :type grants: List[Grant]
        """
        self.openapi_types = {
            'offset': int,
            'limit': int,
            'paging': ResponsePageMetadataPaging,
            'total_results': int,
            'grants': List[Grant]
        }

        self.attribute_map = {
            'offset': 'offset',
            'limit': 'limit',
            'paging': 'paging',
            'total_results': 'totalResults',
            'grants': 'grants'
        }

        self._offset = offset
        self._limit = limit
        self._paging = paging
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
    def paging(self):
        """Gets the paging of this PageOfGrants.


        :return: The paging of this PageOfGrants.
        :rtype: ResponsePageMetadataPaging
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this PageOfGrants.


        :param paging: The paging of this PageOfGrants.
        :type paging: ResponsePageMetadataPaging
        """
        if paging is None:
            raise ValueError("Invalid value for `paging`, must not be `None`")  # noqa: E501

        self._paging = paging

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
