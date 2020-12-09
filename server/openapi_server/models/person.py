# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Person(Model):

    def __init__(self, id=None, first_name=None, last_name=None, email=None):  # noqa: E501
        """Person - a model defined in OpenAPI

        :param id: The id of this Person.  # noqa: E501
        :type id: str
        :param first_name: The first_name of this Person.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this Person.  # noqa: E501
        :type last_name: str
        :param email: The email of this Person.  # noqa: E501
        :type email: str
        """
        self.openapi_types = {
            'id': str,
            'first_name': str,
            'last_name': str,
            'email': str
        }

        self.attribute_map = {
            'id': 'id',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'email': 'email'
        }

        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    @classmethod
    def from_dict(cls, dikt) -> 'Person':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Person of this Person.  # noqa: E501
        :rtype: Person
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Person.

        The ID of a person  # noqa: E501

        :return: The id of this Person.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Person.

        The ID of a person  # noqa: E501

        :param id: The id of this Person.
        :type id: str
        """

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this Person.

        The first name of a person  # noqa: E501

        :return: The first_name of this Person.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Person.

        The first name of a person  # noqa: E501

        :param first_name: The first_name of this Person.
        :type first_name: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501
        if first_name is not None and len(first_name) < 1:
            raise ValueError("Invalid value for `first_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Person.

        The last name of a Person  # noqa: E501

        :return: The last_name of this Person.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Person.

        The last name of a Person  # noqa: E501

        :param last_name: The last_name of this Person.
        :type last_name: str
        """
        if last_name is not None and len(last_name) < 1:
            raise ValueError("Invalid value for `last_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this Person.

        An email address  # noqa: E501

        :return: The email of this Person.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Person.

        An email address  # noqa: E501

        :param email: The email of this Person.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email
