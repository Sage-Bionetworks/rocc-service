# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Challenge(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, challenge_id=None, name=None, start_date=None, end_date=None, url=None, status=None, tags=None, organizers=None):  # noqa: E501
        """Challenge - a model defined in OpenAPI

        :param challenge_id: The challenge_id of this Challenge.  # noqa: E501
        :type challenge_id: str
        :param name: The name of this Challenge.  # noqa: E501
        :type name: str
        :param start_date: The start_date of this Challenge.  # noqa: E501
        :type start_date: date
        :param end_date: The end_date of this Challenge.  # noqa: E501
        :type end_date: date
        :param url: The url of this Challenge.  # noqa: E501
        :type url: str
        :param status: The status of this Challenge.  # noqa: E501
        :type status: str
        :param tags: The tags of this Challenge.  # noqa: E501
        :type tags: List[str]
        :param organizers: The organizers of this Challenge.  # noqa: E501
        :type organizers: List[str]
        """
        self.openapi_types = {
            'challenge_id': str,
            'name': str,
            'start_date': date,
            'end_date': date,
            'url': str,
            'status': str,
            'tags': List[str],
            'organizers': List[str]
        }

        self.attribute_map = {
            'challenge_id': 'challengeId',
            'name': 'name',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'url': 'url',
            'status': 'status',
            'tags': 'tags',
            'organizers': 'organizers'
        }

        self._challenge_id = challenge_id
        self._name = name
        self._start_date = start_date
        self._end_date = end_date
        self._url = url
        self._status = status
        self._tags = tags
        self._organizers = organizers

    @classmethod
    def from_dict(cls, dikt) -> 'Challenge':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Challenge of this Challenge.  # noqa: E501
        :rtype: Challenge
        """
        return util.deserialize_model(dikt, cls)

    @property
    def challenge_id(self):
        """Gets the challenge_id of this Challenge.

        The ID of the challenge  # noqa: E501

        :return: The challenge_id of this Challenge.
        :rtype: str
        """
        return self._challenge_id

    @challenge_id.setter
    def challenge_id(self, challenge_id):
        """Sets the challenge_id of this Challenge.

        The ID of the challenge  # noqa: E501

        :param challenge_id: The challenge_id of this Challenge.
        :type challenge_id: str
        """

        self._challenge_id = challenge_id

    @property
    def name(self):
        """Gets the name of this Challenge.

        The challenge name  # noqa: E501

        :return: The name of this Challenge.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Challenge.

        The challenge name  # noqa: E501

        :param name: The name of this Challenge.
        :type name: str
        """

        self._name = name

    @property
    def start_date(self):
        """Gets the start_date of this Challenge.

        When the challenge started  # noqa: E501

        :return: The start_date of this Challenge.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Challenge.

        When the challenge started  # noqa: E501

        :param start_date: The start_date of this Challenge.
        :type start_date: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Challenge.

        When the challenge ended  # noqa: E501

        :return: The end_date of this Challenge.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Challenge.

        When the challenge ended  # noqa: E501

        :param end_date: The end_date of this Challenge.
        :type end_date: date
        """

        self._end_date = end_date

    @property
    def url(self):
        """Gets the url of this Challenge.

        The URL to the challenge website  # noqa: E501

        :return: The url of this Challenge.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Challenge.

        The URL to the challenge website  # noqa: E501

        :param url: The url of this Challenge.
        :type url: str
        """

        self._url = url

    @property
    def status(self):
        """Gets the status of this Challenge.

        The status of challenge  # noqa: E501

        :return: The status of this Challenge.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Challenge.

        The status of challenge  # noqa: E501

        :param status: The status of this Challenge.
        :type status: str
        """
        allowed_values = ["upcoming", "open", "closed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this Challenge.

        The tags associated to the challenge  # noqa: E501

        :return: The tags of this Challenge.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Challenge.

        The tags associated to the challenge  # noqa: E501

        :param tags: The tags of this Challenge.
        :type tags: List[str]
        """

        self._tags = tags

    @property
    def organizers(self):
        """Gets the organizers of this Challenge.

        The organizers of the challenge  # noqa: E501

        :return: The organizers of this Challenge.
        :rtype: List[str]
        """
        return self._organizers

    @organizers.setter
    def organizers(self, organizers):
        """Sets the organizers of this Challenge.

        The organizers of the challenge  # noqa: E501

        :param organizers: The organizers of this Challenge.
        :type organizers: List[str]
        """

        self._organizers = organizers
