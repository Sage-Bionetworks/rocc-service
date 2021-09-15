# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.page_of_tags_all_of import PageOfTagsAllOf
from openapi_server.models.response_page_metadata import ResponsePageMetadata
from openapi_server.models.response_page_metadata_paging import ResponsePageMetadataPaging
from openapi_server.models.tag import Tag
from openapi_server import util

from openapi_server.models.page_of_tags_all_of import PageOfTagsAllOf  # noqa: E501
from openapi_server.models.response_page_metadata import ResponsePageMetadata  # noqa: E501
from openapi_server.models.response_page_metadata_paging import ResponsePageMetadataPaging  # noqa: E501
from openapi_server.models.tag import Tag  # noqa: E501

class PageOfTags(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, offset=None, limit=None, paging=None, total_results=None, tags=None):  # noqa: E501
        """PageOfTags - a model defined in OpenAPI

        :param offset: The offset of this PageOfTags.  # noqa: E501
        :type offset: int
        :param limit: The limit of this PageOfTags.  # noqa: E501
        :type limit: int
        :param paging: The paging of this PageOfTags.  # noqa: E501
        :type paging: ResponsePageMetadataPaging
        :param total_results: The total_results of this PageOfTags.  # noqa: E501
        :type total_results: int
        :param tags: The tags of this PageOfTags.  # noqa: E501
        :type tags: List[Tag]
        """
        self.openapi_types = {
            'offset': int,
            'limit': int,
            'paging': ResponsePageMetadataPaging,
            'total_results': int,
            'tags': List[Tag]
        }

        self.attribute_map = {
            'offset': 'offset',
            'limit': 'limit',
            'paging': 'paging',
            'total_results': 'totalResults',
            'tags': 'tags'
        }

        self._offset = offset
        self._limit = limit
        self._paging = paging
        self._total_results = total_results
        self._tags = tags

    @classmethod
    def from_dict(cls, dikt) -> 'PageOfTags':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PageOfTags of this PageOfTags.  # noqa: E501
        :rtype: PageOfTags
        """
        return util.deserialize_model(dikt, cls)

    @property
    def offset(self):
        """Gets the offset of this PageOfTags.

        Index of the first result that must be returned  # noqa: E501

        :return: The offset of this PageOfTags.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PageOfTags.

        Index of the first result that must be returned  # noqa: E501

        :param offset: The offset of this PageOfTags.
        :type offset: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this PageOfTags.

        Maximum number of results returned  # noqa: E501

        :return: The limit of this PageOfTags.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PageOfTags.

        Maximum number of results returned  # noqa: E501

        :param limit: The limit of this PageOfTags.
        :type limit: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def paging(self):
        """Gets the paging of this PageOfTags.


        :return: The paging of this PageOfTags.
        :rtype: ResponsePageMetadataPaging
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this PageOfTags.


        :param paging: The paging of this PageOfTags.
        :type paging: ResponsePageMetadataPaging
        """
        if paging is None:
            raise ValueError("Invalid value for `paging`, must not be `None`")  # noqa: E501

        self._paging = paging

    @property
    def total_results(self):
        """Gets the total_results of this PageOfTags.

        Total number of results in the result set  # noqa: E501

        :return: The total_results of this PageOfTags.
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this PageOfTags.

        Total number of results in the result set  # noqa: E501

        :param total_results: The total_results of this PageOfTags.
        :type total_results: int
        """
        if total_results is None:
            raise ValueError("Invalid value for `total_results`, must not be `None`")  # noqa: E501

        self._total_results = total_results

    @property
    def tags(self):
        """Gets the tags of this PageOfTags.

        An array of Tags  # noqa: E501

        :return: The tags of this PageOfTags.
        :rtype: List[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PageOfTags.

        An array of Tags  # noqa: E501

        :param tags: The tags of this PageOfTags.
        :type tags: List[Tag]
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags
