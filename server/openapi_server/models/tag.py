# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util


class Tag(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, tag_id=None, description=None):  # noqa: E501
        """Tag - a model defined in OpenAPI

        :param tag_id: The tag_id of this Tag.  # noqa: E501
        :type tag_id: str
        :param description: The description of this Tag.  # noqa: E501
        :type description: str
        """
        self.openapi_types = {
            'tag_id': str,
            'description': str
        }

        self.attribute_map = {
            'tag_id': 'tagId',
            'description': 'description'
        }

        self._tag_id = tag_id
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'Tag':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Tag of this Tag.  # noqa: E501
        :rtype: Tag
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tag_id(self):
        """Gets the tag_id of this Tag.

        The ID of the tag  # noqa: E501

        :return: The tag_id of this Tag.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """Sets the tag_id of this Tag.

        The ID of the tag  # noqa: E501

        :param tag_id: The tag_id of this Tag.
        :type tag_id: str
        """
        if tag_id is None:
            raise ValueError("Invalid value for `tag_id`, must not be `None`")  # noqa: E501
        if tag_id is not None and len(tag_id) > 60:
            raise ValueError("Invalid value for `tag_id`, length must be less than or equal to `60`")  # noqa: E501
        if tag_id is not None and len(tag_id) < 1:
            raise ValueError("Invalid value for `tag_id`, length must be greater than or equal to `1`")  # noqa: E501
        if tag_id is not None and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', tag_id):  # noqa: E501
            raise ValueError("Invalid value for `tag_id`, must be a follow pattern or equal to `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501

        self._tag_id = tag_id

    @property
    def description(self):
        """Gets the description of this Tag.

        A short description of the tag  # noqa: E501

        :return: The description of this Tag.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Tag.

        A short description of the tag  # noqa: E501

        :param description: The description of this Tag.
        :type description: str
        """

        self._description = description
