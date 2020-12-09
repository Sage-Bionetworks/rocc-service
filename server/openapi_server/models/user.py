# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.organization import Organization
from openapi_server import util


class User(Model):

    def __init__(self, id=None, username=None, password=None, first_name=None, last_name=None, email=None, role='user', organizations=None):  # noqa: E501
        """User - a model defined in OpenAPI

        :param id: The id of this User.  # noqa: E501
        :type id: str
        :param username: The username of this User.  # noqa: E501
        :type username: str
        :param password: The password of this User.  # noqa: E501
        :type password: str
        :param first_name: The first_name of this User.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this User.  # noqa: E501
        :type last_name: str
        :param email: The email of this User.  # noqa: E501
        :type email: str
        :param role: The role of this User.  # noqa: E501
        :type role: str
        :param organizations: The organizations of this User.  # noqa: E501
        :type organizations: List[Organization]
        """
        self.openapi_types = {
            'id': str,
            'username': str,
            'password': str,
            'first_name': str,
            'last_name': str,
            'email': str,
            'role': str,
            'organizations': List[Organization]
        }

        self.attribute_map = {
            'id': 'id',
            'username': 'username',
            'password': 'password',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'email': 'email',
            'role': 'role',
            'organizations': 'organizations'
        }

        self._id = id
        self._username = username
        self._password = password
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._role = role
        self._organizations = organizations

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this User.

        The ID of the user  # noqa: E501

        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

        The ID of the user  # noqa: E501

        :param id: The id of this User.
        :type id: str
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this User.

        The username of the user  # noqa: E501

        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this User.

        The username of the user  # noqa: E501

        :param username: The username of this User.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501
        if username is not None and len(username) < 4:
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `4`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this User.

        The password of the user  # noqa: E501

        :return: The password of this User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this User.

        The password of the user  # noqa: E501

        :param password: The password of this User.
        :type password: str
        """
        if password is not None and len(password) < 3:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `3`")  # noqa: E501

        self._password = password

    @property
    def first_name(self):
        """Gets the first_name of this User.

        The first name of the user  # noqa: E501

        :return: The first_name of this User.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.

        The first name of the user  # noqa: E501

        :param first_name: The first_name of this User.
        :type first_name: str
        """
        if first_name is not None and len(first_name) < 1:
            raise ValueError("Invalid value for `first_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this User.

        The last name of the user  # noqa: E501

        :return: The last_name of this User.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.

        The last name of the user  # noqa: E501

        :param last_name: The last_name of this User.
        :type last_name: str
        """
        if last_name is not None and len(last_name) < 1:
            raise ValueError("Invalid value for `last_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this User.

        An email address  # noqa: E501

        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        An email address  # noqa: E501

        :param email: The email of this User.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def role(self):
        """Gets the role of this User.

        The role of the user  # noqa: E501

        :return: The role of this User.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this User.

        The role of the user  # noqa: E501

        :param role: The role of this User.
        :type role: str
        """
        allowed_values = ["user", "admin"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def organizations(self):
        """Gets the organizations of this User.

        The organizations the user belongs to  # noqa: E501

        :return: The organizations of this User.
        :rtype: List[Organization]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this User.

        The organizations the user belongs to  # noqa: E501

        :param organizations: The organizations of this User.
        :type organizations: List[Organization]
        """

        self._organizations = organizations
