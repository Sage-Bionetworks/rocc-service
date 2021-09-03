# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.challenge_status import ChallengeStatus
import re
from openapi_server import util

from openapi_server.models.challenge_status import ChallengeStatus  # noqa: E501
import re  # noqa: E501

class ChallengeCreateRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, display_name=None, description=None, website_url=None, status=None, start_date=None, end_date=None, platform_id=None):  # noqa: E501
        """ChallengeCreateRequest - a model defined in OpenAPI

        :param name: The name of this ChallengeCreateRequest.  # noqa: E501
        :type name: str
        :param display_name: The display_name of this ChallengeCreateRequest.  # noqa: E501
        :type display_name: str
        :param description: The description of this ChallengeCreateRequest.  # noqa: E501
        :type description: str
        :param website_url: The website_url of this ChallengeCreateRequest.  # noqa: E501
        :type website_url: str
        :param status: The status of this ChallengeCreateRequest.  # noqa: E501
        :type status: ChallengeStatus
        :param start_date: The start_date of this ChallengeCreateRequest.  # noqa: E501
        :type start_date: date
        :param end_date: The end_date of this ChallengeCreateRequest.  # noqa: E501
        :type end_date: date
        :param platform_id: The platform_id of this ChallengeCreateRequest.  # noqa: E501
        :type platform_id: str
        """
        self.openapi_types = {
            'name': str,
            'display_name': str,
            'description': str,
            'website_url': str,
            'status': ChallengeStatus,
            'start_date': date,
            'end_date': date,
            'platform_id': str
        }

        self.attribute_map = {
            'name': 'name',
            'display_name': 'displayName',
            'description': 'description',
            'website_url': 'websiteUrl',
            'status': 'status',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'platform_id': 'platformId'
        }

        self._name = name
        self._display_name = display_name
        self._description = description
        self._website_url = website_url
        self._status = status
        self._start_date = start_date
        self._end_date = end_date
        self._platform_id = platform_id

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

        The name of the a challenge  # noqa: E501

        :return: The name of this ChallengeCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChallengeCreateRequest.

        The name of the a challenge  # noqa: E501

        :param name: The name of this ChallengeCreateRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 60:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `60`")  # noqa: E501
        if name is not None and len(name) < 3:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")  # noqa: E501
        if name is not None and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this ChallengeCreateRequest.


        :return: The display_name of this ChallengeCreateRequest.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ChallengeCreateRequest.


        :param display_name: The display_name of this ChallengeCreateRequest.
        :type display_name: str
        """
        if display_name is not None and len(display_name) > 60:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `60`")  # noqa: E501
        if display_name is not None and len(display_name) < 3:
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `3`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this ChallengeCreateRequest.

        A short description of the challenge  # noqa: E501

        :return: The description of this ChallengeCreateRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChallengeCreateRequest.

        A short description of the challenge  # noqa: E501

        :param description: The description of this ChallengeCreateRequest.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if description is not None and len(description) > 280:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `280`")  # noqa: E501

        self._description = description

    @property
    def website_url(self):
        """Gets the website_url of this ChallengeCreateRequest.


        :return: The website_url of this ChallengeCreateRequest.
        :rtype: str
        """
        return self._website_url

    @website_url.setter
    def website_url(self, website_url):
        """Sets the website_url of this ChallengeCreateRequest.


        :param website_url: The website_url of this ChallengeCreateRequest.
        :type website_url: str
        """

        self._website_url = website_url

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

        self._status = status

    @property
    def start_date(self):
        """Gets the start_date of this ChallengeCreateRequest.


        :return: The start_date of this ChallengeCreateRequest.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ChallengeCreateRequest.


        :param start_date: The start_date of this ChallengeCreateRequest.
        :type start_date: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ChallengeCreateRequest.


        :return: The end_date of this ChallengeCreateRequest.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ChallengeCreateRequest.


        :param end_date: The end_date of this ChallengeCreateRequest.
        :type end_date: date
        """

        self._end_date = end_date

    @property
    def platform_id(self):
        """Gets the platform_id of this ChallengeCreateRequest.

        The unique identifier of a challenge platform  # noqa: E501

        :return: The platform_id of this ChallengeCreateRequest.
        :rtype: str
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        """Sets the platform_id of this ChallengeCreateRequest.

        The unique identifier of a challenge platform  # noqa: E501

        :param platform_id: The platform_id of this ChallengeCreateRequest.
        :type platform_id: str
        """

        self._platform_id = platform_id
