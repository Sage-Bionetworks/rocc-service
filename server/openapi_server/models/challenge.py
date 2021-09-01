# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.challenge_all_of import ChallengeAllOf
from openapi_server.models.challenge_create_request import ChallengeCreateRequest
from openapi_server.models.challenge_create_response import ChallengeCreateResponse
from openapi_server.models.challenge_status import ChallengeStatus
import re
from openapi_server import util

from openapi_server.models.challenge_all_of import ChallengeAllOf  # noqa: E501
from openapi_server.models.challenge_create_request import ChallengeCreateRequest  # noqa: E501
from openapi_server.models.challenge_create_response import ChallengeCreateResponse  # noqa: E501
from openapi_server.models.challenge_status import ChallengeStatus  # noqa: E501
import re  # noqa: E501

class Challenge(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, display_name=None, description=None, website_url=None, status=None, start_date=None, end_date=None, platform_id=None, full_name=None, owner_id=None, created_at=None, updated_at=None):  # noqa: E501
        """Challenge - a model defined in OpenAPI

        :param id: The id of this Challenge.  # noqa: E501
        :type id: str
        :param name: The name of this Challenge.  # noqa: E501
        :type name: str
        :param display_name: The display_name of this Challenge.  # noqa: E501
        :type display_name: str
        :param description: The description of this Challenge.  # noqa: E501
        :type description: str
        :param website_url: The website_url of this Challenge.  # noqa: E501
        :type website_url: str
        :param status: The status of this Challenge.  # noqa: E501
        :type status: ChallengeStatus
        :param start_date: The start_date of this Challenge.  # noqa: E501
        :type start_date: date
        :param end_date: The end_date of this Challenge.  # noqa: E501
        :type end_date: date
        :param platform_id: The platform_id of this Challenge.  # noqa: E501
        :type platform_id: str
        :param full_name: The full_name of this Challenge.  # noqa: E501
        :type full_name: str
        :param owner_id: The owner_id of this Challenge.  # noqa: E501
        :type owner_id: str
        :param created_at: The created_at of this Challenge.  # noqa: E501
        :type created_at: datetime
        :param updated_at: The updated_at of this Challenge.  # noqa: E501
        :type updated_at: datetime
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'display_name': str,
            'description': str,
            'website_url': str,
            'status': ChallengeStatus,
            'start_date': date,
            'end_date': date,
            'platform_id': str,
            'full_name': str,
            'owner_id': str,
            'created_at': datetime,
            'updated_at': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'display_name': 'displayName',
            'description': 'description',
            'website_url': 'websiteUrl',
            'status': 'status',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'platform_id': 'platformId',
            'full_name': 'fullName',
            'owner_id': 'ownerId',
            'created_at': 'createdAt',
            'updated_at': 'updatedAt'
        }

        self._id = id
        self._name = name
        self._display_name = display_name
        self._description = description
        self._website_url = website_url
        self._status = status
        self._start_date = start_date
        self._end_date = end_date
        self._platform_id = platform_id
        self._full_name = full_name
        self._owner_id = owner_id
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

        The unique identifier of the challenge  # noqa: E501

        :return: The id of this Challenge.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Challenge.

        The unique identifier of the challenge  # noqa: E501

        :param id: The id of this Challenge.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Challenge.

        The name of the challenge  # noqa: E501

        :return: The name of this Challenge.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Challenge.

        The name of the challenge  # noqa: E501

        :param name: The name of this Challenge.
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
        """Gets the display_name of this Challenge.


        :return: The display_name of this Challenge.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Challenge.


        :param display_name: The display_name of this Challenge.
        :type display_name: str
        """
        if display_name is not None and len(display_name) > 60:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `60`")  # noqa: E501
        if display_name is not None and len(display_name) < 3:
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `3`")  # noqa: E501

        self._display_name = display_name

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
    def website_url(self):
        """Gets the website_url of this Challenge.


        :return: The website_url of this Challenge.
        :rtype: str
        """
        return self._website_url

    @website_url.setter
    def website_url(self, website_url):
        """Sets the website_url of this Challenge.


        :param website_url: The website_url of this Challenge.
        :type website_url: str
        """

        self._website_url = website_url

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

        self._status = status

    @property
    def start_date(self):
        """Gets the start_date of this Challenge.


        :return: The start_date of this Challenge.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Challenge.


        :param start_date: The start_date of this Challenge.
        :type start_date: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Challenge.


        :return: The end_date of this Challenge.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Challenge.


        :param end_date: The end_date of this Challenge.
        :type end_date: date
        """

        self._end_date = end_date

    @property
    def platform_id(self):
        """Gets the platform_id of this Challenge.

        The unique identifier of a challenge platform  # noqa: E501

        :return: The platform_id of this Challenge.
        :rtype: str
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        """Sets the platform_id of this Challenge.

        The unique identifier of a challenge platform  # noqa: E501

        :param platform_id: The platform_id of this Challenge.
        :type platform_id: str
        """

        self._platform_id = platform_id

    @property
    def full_name(self):
        """Gets the full_name of this Challenge.


        :return: The full_name of this Challenge.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this Challenge.


        :param full_name: The full_name of this Challenge.
        :type full_name: str
        """
        if full_name is None:
            raise ValueError("Invalid value for `full_name`, must not be `None`")  # noqa: E501

        self._full_name = full_name

    @property
    def owner_id(self):
        """Gets the owner_id of this Challenge.

        The unique identifier of an account  # noqa: E501

        :return: The owner_id of this Challenge.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Challenge.

        The unique identifier of an account  # noqa: E501

        :param owner_id: The owner_id of this Challenge.
        :type owner_id: str
        """
        if owner_id is None:
            raise ValueError("Invalid value for `owner_id`, must not be `None`")  # noqa: E501

        self._owner_id = owner_id

    @property
    def created_at(self):
        """Gets the created_at of this Challenge.


        :return: The created_at of this Challenge.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Challenge.


        :param created_at: The created_at of this Challenge.
        :type created_at: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Challenge.


        :return: The updated_at of this Challenge.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Challenge.


        :param updated_at: The updated_at of this Challenge.
        :type updated_at: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at
