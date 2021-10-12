# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.challenge_organizer import ChallengeOrganizer
from openapi_server import util

from openapi_server.models.challenge_organizer import ChallengeOrganizer  # noqa: E501

class ChallengeOrganizerList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, challenge_organizers=None):  # noqa: E501
        """ChallengeOrganizerList - a model defined in OpenAPI

        :param challenge_organizers: The challenge_organizers of this ChallengeOrganizerList.  # noqa: E501
        :type challenge_organizers: List[ChallengeOrganizer]
        """
        self.openapi_types = {
            'challenge_organizers': List[ChallengeOrganizer]
        }

        self.attribute_map = {
            'challenge_organizers': 'challengeOrganizers'
        }

        self._challenge_organizers = challenge_organizers

    @classmethod
    def from_dict(cls, dikt) -> 'ChallengeOrganizerList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChallengeOrganizerList of this ChallengeOrganizerList.  # noqa: E501
        :rtype: ChallengeOrganizerList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def challenge_organizers(self):
        """Gets the challenge_organizers of this ChallengeOrganizerList.

        A list of ChallengeOrganizers  # noqa: E501

        :return: The challenge_organizers of this ChallengeOrganizerList.
        :rtype: List[ChallengeOrganizer]
        """
        return self._challenge_organizers

    @challenge_organizers.setter
    def challenge_organizers(self, challenge_organizers):
        """Sets the challenge_organizers of this ChallengeOrganizerList.

        A list of ChallengeOrganizers  # noqa: E501

        :param challenge_organizers: The challenge_organizers of this ChallengeOrganizerList.
        :type challenge_organizers: List[ChallengeOrganizer]
        """
        if challenge_organizers is None:
            raise ValueError("Invalid value for `challenge_organizers`, must not be `None`")  # noqa: E501

        self._challenge_organizers = challenge_organizers