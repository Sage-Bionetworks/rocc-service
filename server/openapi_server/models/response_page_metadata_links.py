# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ResponsePageMetadataLinks(Model):

    def __init__(self, next=None):  # noqa: E501
        """ResponsePageMetadataLinks - a model defined in OpenAPI

        :param next: The next of this ResponsePageMetadataLinks.  # noqa: E501
        :type next: str
        """
        self.openapi_types = {
            'next': str
        }

        self.attribute_map = {
            'next': 'next'
        }

        self._next = next

    @classmethod
    def from_dict(cls, dikt) -> 'ResponsePageMetadataLinks':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponsePageMetadata_links of this ResponsePageMetadataLinks.  # noqa: E501
        :rtype: ResponsePageMetadataLinks
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next(self):
        """Gets the next of this ResponsePageMetadataLinks.

        Link to the next page of results  # noqa: E501

        :return: The next of this ResponsePageMetadataLinks.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this ResponsePageMetadataLinks.

        Link to the next page of results  # noqa: E501

        :param next: The next of this ResponsePageMetadataLinks.
        :type next: str
        """

        self._next = next
