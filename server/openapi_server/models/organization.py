# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util


class Organization(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, organization_id=None, name=None, short_name=None, url=None):  # noqa: E501
        """Organization - a model defined in OpenAPI

        :param organization_id: The organization_id of this Organization.  # noqa: E501
        :type organization_id: str
        :param name: The name of this Organization.  # noqa: E501
        :type name: str
        :param short_name: The short_name of this Organization.  # noqa: E501
        :type short_name: str
        :param url: The url of this Organization.  # noqa: E501
        :type url: str
        """
        self.openapi_types = {
            'organization_id': str,
            'name': str,
            'short_name': str,
            'url': str
        }

        self.attribute_map = {
            'organization_id': 'organizationId',
            'name': 'name',
            'short_name': 'shortName',
            'url': 'url'
        }

        self._organization_id = organization_id
        self._name = name
        self._short_name = short_name
        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'Organization':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Organization of this Organization.  # noqa: E501
        :rtype: Organization
        """
        return util.deserialize_model(dikt, cls)

    @property
    def organization_id(self):
        """Gets the organization_id of this Organization.

        The ID of the organization  # noqa: E501

        :return: The organization_id of this Organization.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Organization.

        The ID of the organization  # noqa: E501

        :param organization_id: The organization_id of this Organization.
        :type organization_id: str
        """
        if organization_id is None:
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501
        if organization_id is not None and len(organization_id) > 60:
            raise ValueError("Invalid value for `organization_id`, length must be less than or equal to `60`")  # noqa: E501
        if organization_id is not None and len(organization_id) < 3:
            raise ValueError("Invalid value for `organization_id`, length must be greater than or equal to `3`")  # noqa: E501
        if organization_id is not None and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', organization_id):  # noqa: E501
            raise ValueError("Invalid value for `organization_id`, must be a follow pattern or equal to `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def name(self):
        """Gets the name of this Organization.

        The organization name  # noqa: E501

        :return: The name of this Organization.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Organization.

        The organization name  # noqa: E501

        :param name: The name of this Organization.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def short_name(self):
        """Gets the short_name of this Organization.

        The organization short name  # noqa: E501

        :return: The short_name of this Organization.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this Organization.

        The organization short name  # noqa: E501

        :param short_name: The short_name of this Organization.
        :type short_name: str
        """

        self._short_name = short_name

    @property
    def url(self):
        """Gets the url of this Organization.

        The URL to the homepage of the organization  # noqa: E501

        :return: The url of this Organization.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Organization.

        The URL to the homepage of the organization  # noqa: E501

        :param url: The url of this Organization.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url
