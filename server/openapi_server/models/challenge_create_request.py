# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.challenge_results import ChallengeResults
from openapi_server.models.challenge_status import ChallengeStatus
from openapi_server import util


class ChallengeCreateRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, start_date=None, end_date=None, url=None, status=None, tags=None, challenge_results=None, organizers=None):  # noqa: E501
        """ChallengeCreateRequest - a model defined in OpenAPI

        :param name: The name of this ChallengeCreateRequest.  # noqa: E501
        :type name: str
        :param start_date: The start_date of this ChallengeCreateRequest.  # noqa: E501
        :type start_date: date
        :param end_date: The end_date of this ChallengeCreateRequest.  # noqa: E501
        :type end_date: date
        :param url: The url of this ChallengeCreateRequest.  # noqa: E501
        :type url: str
        :param status: The status of this ChallengeCreateRequest.  # noqa: E501
        :type status: ChallengeStatus
        :param tags: The tags of this ChallengeCreateRequest.  # noqa: E501
        :type tags: List[str]
        :param challenge_results: The challenge_results of this ChallengeCreateRequest.  # noqa: E501
        :type challenge_results: ChallengeResults
        :param organizers: The organizers of this ChallengeCreateRequest.  # noqa: E501
        :type organizers: List[str]
        """
        self.openapi_types = {
            'name': str,
            'start_date': date,
            'end_date': date,
            'url': str,
            'status': ChallengeStatus,
            'tags': List[str],
            'challenge_results': ChallengeResults,
            'organizers': List[str]
        }

        self.attribute_map = {
            'name': 'name',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'url': 'url',
            'status': 'status',
            'tags': 'tags',
            'challenge_results': 'challengeResults',
            'organizers': 'organizers'
        }

        self._name = name
        self._start_date = start_date
        self._end_date = end_date
        self._url = url
        self._status = status
        self._tags = tags
        self._challenge_results = challenge_results
        self._organizers = organizers

    @classmethod
    def from_dict(cls, dikt) -> 'ChallengeCreateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChallengeCreateRequest of this ChallengeCreateRequest.  # noqa: E501
        :rtype: ChallengeCreateRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this ChallengeCreateRequest.

        The challenge name  # noqa: E501

        :return: The name of this ChallengeCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChallengeCreateRequest.

        The challenge name  # noqa: E501

        :param name: The name of this ChallengeCreateRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def start_date(self):
        """Gets the start_date of this ChallengeCreateRequest.

        When the challenge started  # noqa: E501

        :return: The start_date of this ChallengeCreateRequest.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ChallengeCreateRequest.

        When the challenge started  # noqa: E501

        :param start_date: The start_date of this ChallengeCreateRequest.
        :type start_date: date
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ChallengeCreateRequest.

        When the challenge ended  # noqa: E501

        :return: The end_date of this ChallengeCreateRequest.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ChallengeCreateRequest.

        When the challenge ended  # noqa: E501

        :param end_date: The end_date of this ChallengeCreateRequest.
        :type end_date: date
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def url(self):
        """Gets the url of this ChallengeCreateRequest.

        The URL to the challenge website  # noqa: E501

        :return: The url of this ChallengeCreateRequest.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ChallengeCreateRequest.

        The URL to the challenge website  # noqa: E501

        :param url: The url of this ChallengeCreateRequest.
        :type url: str
        """

        self._url = url

    @property
    def status(self):
        """Gets the status of this ChallengeCreateRequest.


        :return: The status of this ChallengeCreateRequest.
        :rtype: ChallengeStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ChallengeCreateRequest.


        :param status: The status of this ChallengeCreateRequest.
        :type status: ChallengeStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this ChallengeCreateRequest.

        The tags associated to the challenge  # noqa: E501

        :return: The tags of this ChallengeCreateRequest.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ChallengeCreateRequest.

        The tags associated to the challenge  # noqa: E501

        :param tags: The tags of this ChallengeCreateRequest.
        :type tags: List[str]
        """

        self._tags = tags

    @property
    def challenge_results(self):
        """Gets the challenge_results of this ChallengeCreateRequest.


        :return: The challenge_results of this ChallengeCreateRequest.
        :rtype: ChallengeResults
        """
        return self._challenge_results

    @challenge_results.setter
    def challenge_results(self, challenge_results):
        """Sets the challenge_results of this ChallengeCreateRequest.


        :param challenge_results: The challenge_results of this ChallengeCreateRequest.
        :type challenge_results: ChallengeResults
        """

        self._challenge_results = challenge_results

    @property
    def organizers(self):
        """Gets the organizers of this ChallengeCreateRequest.

        The organizers of the challenge  # noqa: E501

        :return: The organizers of this ChallengeCreateRequest.
        :rtype: List[str]
        """
        return self._organizers

    @organizers.setter
    def organizers(self, organizers):
        """Sets the organizers of this ChallengeCreateRequest.

        The organizers of the challenge  # noqa: E501

        :param organizers: The organizers of this ChallengeCreateRequest.
        :type organizers: List[str]
        """

        self._organizers = organizers