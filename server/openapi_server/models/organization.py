# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Organization(Model):

    def __init__(self, id=None, name=None, url=None):  # noqa: E501
        """Organization - a model defined in OpenAPI

        :param id: The id of this Organization.  # noqa: E501
        :type id: str
        :param name: The name of this Organization.  # noqa: E501
        :type name: str
        :param url: The url of this Organization.  # noqa: E501
        :type url: str
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'url': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'url': 'url'
        }

        self._id = id
        self._name = name
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
    def id(self):
        """Gets the id of this Organization.

        The ID of the organization  # noqa: E501

        :return: The id of this Organization.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Organization.

        The ID of the organization  # noqa: E501

        :param id: The id of this Organization.
        :type id: str
        """

        self._id = id

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
