# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.organization import Organization
from openapi_server import util


class Grant(Model):

    def __init__(self, id=None, name=None, description=None, sponsor=None, url=None):  # noqa: E501
        """Grant - a model defined in OpenAPI

        :param id: The id of this Grant.  # noqa: E501
        :type id: str
        :param name: The name of this Grant.  # noqa: E501
        :type name: str
        :param description: The description of this Grant.  # noqa: E501
        :type description: str
        :param sponsor: The sponsor of this Grant.  # noqa: E501
        :type sponsor: Organization
        :param url: The url of this Grant.  # noqa: E501
        :type url: str
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'description': str,
            'sponsor': Organization,
            'url': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'sponsor': 'sponsor',
            'url': 'url'
        }

        self._id = id
        self._name = name
        self._description = description
        self._sponsor = sponsor
        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'Grant':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Grant of this Grant.  # noqa: E501
        :rtype: Grant
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Grant.

        The ID of the grant  # noqa: E501

        :return: The id of this Grant.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Grant.

        The ID of the grant  # noqa: E501

        :param id: The id of this Grant.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Grant.

        The grant name  # noqa: E501

        :return: The name of this Grant.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Grant.

        The grant name  # noqa: E501

        :param name: The name of this Grant.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Grant.

        A description of the grant  # noqa: E501

        :return: The description of this Grant.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Grant.

        A description of the grant  # noqa: E501

        :param description: The description of this Grant.
        :type description: str
        """

        self._description = description

    @property
    def sponsor(self):
        """Gets the sponsor of this Grant.


        :return: The sponsor of this Grant.
        :rtype: Organization
        """
        return self._sponsor

    @sponsor.setter
    def sponsor(self, sponsor):
        """Sets the sponsor of this Grant.


        :param sponsor: The sponsor of this Grant.
        :type sponsor: Organization
        """
        if sponsor is None:
            raise ValueError("Invalid value for `sponsor`, must not be `None`")  # noqa: E501

        self._sponsor = sponsor

    @property
    def url(self):
        """Gets the url of this Grant.

        The URL to the grant  # noqa: E501

        :return: The url of this Grant.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Grant.

        The URL to the grant  # noqa: E501

        :param url: The url of this Grant.
        :type url: str
        """

        self._url = url
