# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.response_page_metadata import ResponsePageMetadata  # noqa: E501
from openapi_server.models.response_page_metadata_links import ResponsePageMetadataLinks  # noqa: E501
from openapi_server.models.tag import Tag  # noqa: E501
from openapi_server import util


class PageOfTags(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, offset=None, limit=None, links=None, tags=None):  # noqa: E501
        """PageOfTags - a model defined in OpenAPI

        :param offset: The offset of this PageOfTags.  # noqa: E501
        :type offset: int
        :param limit: The limit of this PageOfTags.  # noqa: E501
        :type limit: int
        :param links: The links of this PageOfTags.  # noqa: E501
        :type links: ResponsePageMetadataLinks
        :param tags: The tags of this PageOfTags.  # noqa: E501
        :type tags: List[Tag]
        """
        self.openapi_types = {
            'offset': int,
            'limit': int,
            'links': ResponsePageMetadataLinks,
            'tags': List[Tag]
        }

        self.attribute_map = {
            'offset': 'offset',
            'limit': 'limit',
            'links': 'links',
            'tags': 'tags'
        }

        self._offset = offset
        self._limit = limit
        self._links = links
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
    def links(self):
        """Gets the links of this PageOfTags.


        :return: The links of this PageOfTags.
        :rtype: ResponsePageMetadataLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PageOfTags.


        :param links: The links of this PageOfTags.
        :type links: ResponsePageMetadataLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

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

        self._tags = tags