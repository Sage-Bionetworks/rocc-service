# coding: utf-8

from __future__ import absolute_import
from datetime import date
import unittest

from flask import json

from openapi_server.dbmodels.challenge import Challenge as DbChallenge
from openapi_server.dbmodels.person import Person as DbPerson
from openapi_server.dbmodels.tag import Tag as DbTag
from openapi_server.test.integration import BaseTestCase
from openapi_server.test.integration import util


class TestChallengeController(BaseTestCase):
    """ChallengeController integration test stubs"""

    def setUp(self):
        util.connect_db()
        DbChallenge.objects().delete()
        DbPerson.objects().delete()
        DbTag.objects().delete()
        util.create_test_tag("awesome-tag")

    def tearDown(self):
        util.disconnect_db()

    def test_create_challenge(self):
        """Test case for create_challenge

        Create a challenge
        """
        person = util.create_test_person(
            organizations=['awesome-organization']).to_dict()
        challenge = {
            "name": "awesome-challenge",
            "startDate": date(2020, 12, 1),
            "endDate": date(2020, 12, 31),
            "url": "https://www.synapse.org/",
            "status": "upcoming",
            "organizers": [person.get("personId")],
            "tags": ["awesome-tag"]
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        response = self.client.open(
            "/api/v1/challenges",
            method="POST",
            headers=headers,
            data=json.dumps(challenge),
            content_type="application/json")
        self.assert200(response,
                       "Response body is : " + response.data.decode("utf-8"))

    def test_delete_challenge(self):
        """Test case for delete_challenge

        Delete a challenge
        """
        person = util.create_test_person(
            organizations=['awesome-organization'])
        challenge = util.create_test_challenge(
            organizers=[person.personId],
            tags=["awesome-tag"])
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open(
            "/api/v1/challenges/{challenge_id}".format(
                challenge_id=challenge.challengeId),
            method="DELETE",
            headers=headers)
        self.assert200(response,
                       "Response body is : " + response.data.decode("utf-8"))

    def test_get_challenge(self):
        """Test case for get_challenge

        Get a challenge
        """
        person = util.create_test_person(
            organizations=['awesome-organization'])
        challenge = util.create_test_challenge(
            organizers=[person.personId],
            tags=["awesome-tag"])
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open(
            "/api/v1/challenges/{challenge_id}".format(
                challenge_id=challenge.challengeId),
            method="GET",
            headers=headers)
        self.assert200(response,
                       "Response body is : " + response.data.decode("utf-8"))

    def test_list_challenges(self):
        """Test case for list_challenges

        Get all challenges
        """
        person = util.create_test_person(
            organizations=['awesome-organization'])
        util.create_test_challenge(
            organizers=[person.personId],
            tags=["awesome-tag"])
        query_string = [("limit", 10),
                        ("offset", 0),
                        ('filter_', {
                            # TODO: add values to increase coverage
                        })]
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open(
            "/api/v1/challenges",
            method="GET",
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
