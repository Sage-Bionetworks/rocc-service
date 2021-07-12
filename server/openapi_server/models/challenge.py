# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.challenge_all_of import ChallengeAllOf
from openapi_server.models.challenge_create_request import ChallengeCreateRequest
from openapi_server.models.challenge_create_response import ChallengeCreateResponse
from openapi_server.models.challenge_platform_id import ChallengePlatformId
from openapi_server.models.challenge_status import ChallengeStatus
from openapi_server import util

from openapi_server.models.challenge_all_of import ChallengeAllOf  # noqa: E501
from openapi_server.models.challenge_create_request import ChallengeCreateRequest  # noqa: E501
from openapi_server.models.challenge_create_response import ChallengeCreateResponse  # noqa: E501
from openapi_server.models.challenge_platform_id import ChallengePlatformId  # noqa: E501
from openapi_server.models.challenge_status import ChallengeStatus  # noqa: E501

class Challenge(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, description=None, summary=None, start_date=None, end_date=None, url=None, status=None, tag_ids=None, organizer_ids=None, data_provider_ids=None, grant_ids=None, platform_id=None, created_at=None, updated_at=None):  # noqa: E501
        """Challenge - a model defined in OpenAPI

        :param id: The id of this Challenge.  # noqa: E501
        :type id: str
        :param name: The name of this Challenge.  # noqa: E501
        :type name: str
        :param description: The description of this Challenge.  # noqa: E501
        :type description: str
        :param summary: The summary of this Challenge.  # noqa: E501
        :type summary: str
        :param start_date: The start_date of this Challenge.  # noqa: E501
        :type start_date: date
        :param end_date: The end_date of this Challenge.  # noqa: E501
        :type end_date: date
        :param url: The url of this Challenge.  # noqa: E501
        :type url: str
        :param status: The status of this Challenge.  # noqa: E501
        :type status: ChallengeStatus
        :param tag_ids: The tag_ids of this Challenge.  # noqa: E501
        :type tag_ids: List[str]
        :param organizer_ids: The organizer_ids of this Challenge.  # noqa: E501
        :type organizer_ids: List[str]
        :param data_provider_ids: The data_provider_ids of this Challenge.  # noqa: E501
        :type data_provider_ids: List[str]
        :param grant_ids: The grant_ids of this Challenge.  # noqa: E501
        :type grant_ids: List[str]
        :param platform_id: The platform_id of this Challenge.  # noqa: E501
        :type platform_id: ChallengePlatformId
        :param created_at: The created_at of this Challenge.  # noqa: E501
        :type created_at: datetime
        :param updated_at: The updated_at of this Challenge.  # noqa: E501
        :type updated_at: datetime
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'description': str,
            'summary': str,
            'start_date': date,
            'end_date': date,
            'url': str,
            'status': ChallengeStatus,
            'tag_ids': List[str],
            'organizer_ids': List[str],
            'data_provider_ids': List[str],
            'grant_ids': List[str],
            'platform_id': ChallengePlatformId,
            'created_at': datetime,
            'updated_at': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'summary': 'summary',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'url': 'url',
            'status': 'status',
            'tag_ids': 'tagIds',
            'organizer_ids': 'organizerIds',
            'data_provider_ids': 'dataProviderIds',
            'grant_ids': 'grantIds',
            'platform_id': 'platformId',
            'created_at': 'createdAt',
            'updated_at': 'updatedAt'
        }

        self._id = id
        self._name = name
        self._description = description
        self._summary = summary
        self._start_date = start_date
        self._end_date = end_date
        self._url = url
        self._status = status
        self._tag_ids = tag_ids
        self._organizer_ids = organizer_ids
        self._data_provider_ids = data_provider_ids
        self._grant_ids = grant_ids
        self._platform_id = platform_id
        self._created_at = created_at
        self._updated_at = updated_at

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
    def id(self):
        """Gets the id of this Challenge.

        The ID of the challenge  # noqa: E501

        :return: The id of this Challenge.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Challenge.

        The ID of the challenge  # noqa: E501

        :param id: The id of this Challenge.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 60:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `60`")  # noqa: E501
        if name is not None and len(name) < 3:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Challenge.

        A short description of the challenge  # noqa: E501

        :return: The description of this Challenge.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Challenge.

        A short description of the challenge  # noqa: E501

        :param description: The description of this Challenge.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if description is not None and len(description) > 280:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `280`")  # noqa: E501

        self._description = description

    @property
    def summary(self):
        """Gets the summary of this Challenge.

        The summary of challenge  # noqa: E501

        :return: The summary of this Challenge.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this Challenge.

        The summary of challenge  # noqa: E501

        :param summary: The summary of this Challenge.
        :type summary: str
        """

        self._summary = summary

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
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def status(self):
        """Gets the status of this Challenge.


        :return: The status of this Challenge.
        :rtype: ChallengeStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Challenge.


        :param status: The status of this Challenge.
        :type status: ChallengeStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def tag_ids(self):
        """Gets the tag_ids of this Challenge.

        The tags associated to the challenge  # noqa: E501

        :return: The tag_ids of this Challenge.
        :rtype: List[str]
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        """Sets the tag_ids of this Challenge.

        The tags associated to the challenge  # noqa: E501

        :param tag_ids: The tag_ids of this Challenge.
        :type tag_ids: List[str]
        """
        if tag_ids is None:
            raise ValueError("Invalid value for `tag_ids`, must not be `None`")  # noqa: E501

        self._tag_ids = tag_ids

    @property
    def organizer_ids(self):
        """Gets the organizer_ids of this Challenge.

        The organizers of the challenge  # noqa: E501

        :return: The organizer_ids of this Challenge.
        :rtype: List[str]
        """
        return self._organizer_ids

    @organizer_ids.setter
    def organizer_ids(self, organizer_ids):
        """Sets the organizer_ids of this Challenge.

        The organizers of the challenge  # noqa: E501

        :param organizer_ids: The organizer_ids of this Challenge.
        :type organizer_ids: List[str]
        """
        if organizer_ids is None:
            raise ValueError("Invalid value for `organizer_ids`, must not be `None`")  # noqa: E501

        self._organizer_ids = organizer_ids

    @property
    def data_provider_ids(self):
        """Gets the data_provider_ids of this Challenge.

        The organizations contributing the data  # noqa: E501

        :return: The data_provider_ids of this Challenge.
        :rtype: List[str]
        """
        return self._data_provider_ids

    @data_provider_ids.setter
    def data_provider_ids(self, data_provider_ids):
        """Sets the data_provider_ids of this Challenge.

        The organizations contributing the data  # noqa: E501

        :param data_provider_ids: The data_provider_ids of this Challenge.
        :type data_provider_ids: List[str]
        """
        if data_provider_ids is None:
            raise ValueError("Invalid value for `data_provider_ids`, must not be `None`")  # noqa: E501

        self._data_provider_ids = data_provider_ids

    @property
    def grant_ids(self):
        """Gets the grant_ids of this Challenge.

        The grants supporting this challenge  # noqa: E501

        :return: The grant_ids of this Challenge.
        :rtype: List[str]
        """
        return self._grant_ids

    @grant_ids.setter
    def grant_ids(self, grant_ids):
        """Sets the grant_ids of this Challenge.

        The grants supporting this challenge  # noqa: E501

        :param grant_ids: The grant_ids of this Challenge.
        :type grant_ids: List[str]
        """
        if grant_ids is None:
            raise ValueError("Invalid value for `grant_ids`, must not be `None`")  # noqa: E501

        self._grant_ids = grant_ids

    @property
    def platform_id(self):
        """Gets the platform_id of this Challenge.


        :return: The platform_id of this Challenge.
        :rtype: ChallengePlatformId
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        """Sets the platform_id of this Challenge.


        :param platform_id: The platform_id of this Challenge.
        :type platform_id: ChallengePlatformId
        """
        if platform_id is None:
            raise ValueError("Invalid value for `platform_id`, must not be `None`")  # noqa: E501

        self._platform_id = platform_id

    @property
    def created_at(self):
        """Gets the created_at of this Challenge.

        When this challenge has been created  # noqa: E501

        :return: The created_at of this Challenge.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Challenge.

        When this challenge has been created  # noqa: E501

        :param created_at: The created_at of this Challenge.
        :type created_at: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Challenge.

        When this challenge has last been updated  # noqa: E501

        :return: The updated_at of this Challenge.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Challenge.

        When this challenge has last been updated  # noqa: E501

        :param updated_at: The updated_at of this Challenge.
        :type updated_at: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at
