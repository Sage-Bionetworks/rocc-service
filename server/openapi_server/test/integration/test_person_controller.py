# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from bson.objectid import ObjectId

from openapi_server.dbmodels.organization import Organization as DbOrganization
from openapi_server.dbmodels.person import Person as DbPerson
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


class TestPersonController(BaseTestCase):
    """PersonController integration test stubs"""

    def setUp(self):
        util.connect_db()
        DbOrganization.objects.delete()
        DbPerson.objects.delete()
        util.create_test_organization("awesome-organization")

    def tearDown(self):
        util.disconnect_db()

    def test_create_person_with_status201(self):
        """Test case for create_person

        Create a person (201)
        """
        person = {
            'firstName': "John",
            'lastName': "Smith",
            'organizations': ["awesome-organization"],
            'email': "john.smith@example.com"
        }
        response = self.client.open(
            "/api/v1/persons",
            method="POST",
            headers=REQUEST_HEADERS,
            data=json.dumps(person)
        )
        self.assertStatus(
            response, 201,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_create_person_with_status400(self):
        """Test case for create_person

        Create a (non-JSON) person (400)
        """
        person = {
            'firstName': "John",
            'lastName': "Smith",
            'organizations': ["awesome-organization"],
            'email': "john.smith@example.com"
        }
        response = self.client.open(
            "/api/v1/persons",
            method="POST",
            headers=REQUEST_HEADERS,
            data=person
        )
        self.assert400(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_create_empty_person_with_status400(self):
        """Test case for create_person

        Create an empty person (400)
        """
        person = {}
        response = self.client.open(
            "/api/v1/persons",
            method="POST",
            headers=REQUEST_HEADERS,
            data=person
        )
        self.assert400(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_delete_person_with_status200(self):
        """Test case for delete_person

        Delete an existing person (200)
        """
        person = util.create_test_person(["awesome-organization"])
        response = self.client.open(
            f"/api/v1/persons/{person.personId}",
            method="DELETE",
            headers=RESPONSE_HEADERS)
        self.assert200(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_delete_person_with_status404(self):
        """Test case for delete_person

        Delete an unknown person (404)
        """
        person_id = ObjectId()
        response = self.client.open(
            f"/api/v1/persons/{person_id}",
            method="DELETE",
            headers=RESPONSE_HEADERS)
        self.assert404(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_get_person_with_status200(self):
        """Test case for get_person

        Get an existing person (200)
        """
        person = util.create_test_person(["awesome-organization"])
        response = self.client.open(
            f"/api/v1/persons/{person.personId}",
            method="GET",
            headers=RESPONSE_HEADERS)
        self.assert200(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_get_person_with_status404(self):
        """Test case for get_person

        Get an unknown person (404)
        """
        person_id = ObjectId()
        response = self.client.open(
            f"/api/v1/persons/{person_id}",
            method="GET",
            headers=RESPONSE_HEADERS)
        self.assert404(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_list_persons_with_status200(self):
        """Test case for list_persons

        Get all persons (200)
        """
        util.create_test_person(["awesome-organization"])
        query_string = [("limit", 10),
                        ("offset", 0),
                        ("filter_", {
                            # TODO: add values to increase coverage
                        })]
        response = self.client.open(
            "/api/v1/persons",
            method="GET",
            headers=RESPONSE_HEADERS,
            query_string=query_string)
        self.assert200(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_list_persons_with_status400(self):
        """Test case for list_persons

        Get all persons using an invalid query (400)
        """
        util.create_test_person(["awesome-organization"])
        query_string = [("limit", "no-limit"),
                        ("offset", "none"),
                        ("filter_", {
                            # TODO: add values to increase coverage
                        })]
        response = self.client.open(
            "/api/v1/persons",
            method="GET",
            headers=RESPONSE_HEADERS,
            query_string=query_string)
        self.assert400(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )


if __name__ == "__main__":
    unittest.main()
