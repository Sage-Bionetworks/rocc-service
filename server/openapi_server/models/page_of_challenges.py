# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.challenge import Challenge  # noqa: E501
from openapi_server.models.response_page_metadata import ResponsePageMetadata  # noqa: E501
from openapi_server.models.response_page_metadata_links import ResponsePageMetadataLinks  # noqa: E501
from openapi_server import util


class PageOfChallenges(Model):

    def __init__(self, offset=None, limit=None, links=None, challenges=None):  # noqa: E501
        """PageOfChallenges - a model defined in OpenAPI

        :param offset: The offset of this PageOfChallenges.  # noqa: E501
        :type offset: int
        :param limit: The limit of this PageOfChallenges.  # noqa: E501
        :type limit: int
        :param links: The links of this PageOfChallenges.  # noqa: E501
        :type links: ResponsePageMetadataLinks
        :param challenges: The challenges of this PageOfChallenges.  # noqa: E501
        :type challenges: List[Challenge]
        """
        self.openapi_types = {
            'offset': int,
            'limit': int,
            'links': ResponsePageMetadataLinks,
            'challenges': List[Challenge]
        }

        self.attribute_map = {
            'offset': 'offset',
            'limit': 'limit',
            'links': 'links',
            'challenges': 'challenges'
        }

        self._offset = offset
        self._limit = limit
        self._links = links
        self._challenges = challenges

    @classmethod
    def from_dict(cls, dikt) -> 'PageOfChallenges':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PageOfChallenges of this PageOfChallenges.  # noqa: E501
        :rtype: PageOfChallenges
        """
        return util.deserialize_model(dikt, cls)

    @property
    def offset(self):
        """Gets the offset of this PageOfChallenges.

        Index of the first result that must be returned  # noqa: E501

        :return: The offset of this PageOfChallenges.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PageOfChallenges.

        Index of the first result that must be returned  # noqa: E501

        :param offset: The offset of this PageOfChallenges.
        :type offset: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this PageOfChallenges.

        Maximum number of results returned  # noqa: E501

        :return: The limit of this PageOfChallenges.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PageOfChallenges.

        Maximum number of results returned  # noqa: E501

        :param limit: The limit of this PageOfChallenges.
        :type limit: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def links(self):
        """Gets the links of this PageOfChallenges.


        :return: The links of this PageOfChallenges.
        :rtype: ResponsePageMetadataLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PageOfChallenges.


        :param links: The links of this PageOfChallenges.
        :type links: ResponsePageMetadataLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def challenges(self):
        """Gets the challenges of this PageOfChallenges.

        An array of Challenges  # noqa: E501

        :return: The challenges of this PageOfChallenges.
        :rtype: List[Challenge]
        """
        return self._challenges

    @challenges.setter
    def challenges(self, challenges):
        """Sets the challenges of this PageOfChallenges.

        An array of Challenges  # noqa: E501

        :param challenges: The challenges of this PageOfChallenges.
        :type challenges: List[Challenge]
        """

        self._challenges = challenges
