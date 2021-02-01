# coding: utf-8

from __future__ import absolute_import
from datetime import date
import unittest

from flask import json
from bson.objectid import ObjectId

from openapi_server.dbmodels.challenge import Challenge as DbChallenge
from openapi_server.dbmodels.person import Person as DbPerson
from openapi_server.dbmodels.tag import Tag as DbTag
from openapi_server.test.integration import BaseTestCase
from openapi_server.test.integration import util


REQUEST_HEADERS = {
    'Accept': "application/json",
    'Content-Type': "application/json",
}
RESPONSE_HEADERS = {
    'Accept': "application/json",
}

# TODO: mock 409 and 500 reponses


class TestChallengeController(BaseTestCase):
    """ChallengeController integration test stubs"""

    def setUp(self):
        util.connect_db()
        DbChallenge.objects.delete()
        DbPerson.objects.delete()
        DbTag.objects.delete()
        util.create_test_tag("awesome-tag")

    def tearDown(self):
        util.disconnect_db()

    def test_create_challenge_with_status201(self):
        """Test case for create_challenge

        Create a challenge (201)
        """
        person = util.create_test_person(["awesome-organization"]).to_dict()
        challenge = {
            'name': "awesome-challenge",
            'startDate': date(2020, 12, 1),
            'endDate': date(2020, 12, 31),
            'url': "https://www.synapse.org/",
            'status': "upcoming",
            'organizers': [person.get("personId")],
            'tags': ["awesome-tag"],
            'challengeResults': {}
        }
        response = self.client.open(
            "/api/v1/challenges",
            method="POST",
            headers=REQUEST_HEADERS,
            data=json.dumps(challenge)
        )
        self.assertStatus(
            response, 201,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_create_challenge_with_status400(self):
        """Test case for create_challenge

        Create a (non-JSON) challenge (400)
        """
        person = util.create_test_person(["awesome-organization"]).to_dict()
        challenge = {
            'name': "awesome-challenge",
            'startDate': date(2020, 12, 1),
            'endDate': date(2020, 12, 31),
            'url': "https://www.synapse.org/",
            'status': "upcoming",
            'organizers': [person.get("personId")],
            'tags': ["awesome-tag"],
            'challengeResults': {}
        }
        response = self.client.open(
            "/api/v1/challenges",
            method="POST",
            headers=REQUEST_HEADERS,
            data=challenge
        )
        self.assert400(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_create_empty_challenge_with_status400(self):
        """Test case for create_challenge

        Create an empty challenge (400)
        """
        challenge = {}
        response = self.client.open(
            "/api/v1/challenges",
            method="POST",
            headers=REQUEST_HEADERS,
            data=json.dumps(challenge)
        )
        self.assert400(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_delete_challenge_with_status200(self):
        """Test case for delete_challenge

        Delete an existing challenge (200)
        """
        person = util.create_test_person(["awesome-organization"])
        challenge = util.create_test_challenge(
            organizers=[person.personId],
            tags=["awesome-tag"]
        )
        response = self.client.open(
            f"/api/v1/challenges/{challenge.challengeId}",
            method="DELETE",
            headers=RESPONSE_HEADERS
        )
        self.assert200(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_delete_challenge_with_status404(self):
        """Test case for delete_challenge

        Delete an unknown challenge (404)
        """
        challenge_id = ObjectId()
        response = self.client.open(
            f"/api/v1/challenges/{challenge_id}",
            method="DELETE",
            headers=RESPONSE_HEADERS
        )
        self.assert404(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_get_challenge_with_status200(self):
        """Test case for get_challenge

        Get an existing challenge (200)
        """
        person = util.create_test_person(["awesome-organization"])
        challenge = util.create_test_challenge(
            organizers=[person.personId],
            tags=["awesome-tag"]
        )
        response = self.client.open(
            f"/api/v1/challenges/{challenge.challengeId}",
            method="GET",
            headers=RESPONSE_HEADERS
        )
        self.assert200(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_get_challenge_with_status404(self):
        """Test case for get_challenge

        Get an unknown challenge (404)
        """
        challenge_id = ObjectId()
        response = self.client.open(
            f"/api/v1/challenges/{challenge_id}",
            method="GET",
            headers=RESPONSE_HEADERS
        )
        self.assert404(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_list_challenges_with_status200(self):
        """Test case for list_challenges

        Get all challenges
        """
        person = util.create_test_person(["awesome-organization"])
        util.create_test_challenge(
            organizers=[person.personId],
            tags=["awesome-tag"]
        )
        query_string = [("limit", 10),
                        ("offset", 0),
                        ("filter_", {
                            # TODO: add values to increase coverage
                        })]
        response = self.client.open(
            "/api/v1/challenges",
            method="GET",
            headers=RESPONSE_HEADERS,
            query_string=query_string
        )
        self.assert200(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_list_challenges_with_status400(self):
        """Test case for list_challenges

        Get all challenges using an invalid query (400)
        """
        person = util.create_test_person(["awesome-organization"])
        util.create_test_challenge(
            organizers=[person.personId],
            tags=["awesome-tag"]
        )
        query_string = [("limit", "no-limit"),
                        ("offset", "none"),
                        ("filter_", {
                            # TODO: add values to increase coverage
                        })]
        response = self.client.open(
            "/api/v1/challenges",
            method="GET",
            headers=RESPONSE_HEADERS,
            query_string=query_string
        )
        self.assert400(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )


if __name__ == "__main__":
    unittest.main()
