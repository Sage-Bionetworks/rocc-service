# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json

from mongoengine.errors import DoesNotExist, NotUniqueError
from openapi_server.dbmodels.grant import Grant as DbGrant
from openapi_server.test.integration import BaseTestCase
from openapi_server.test.integration import util
from bson.objectid import ObjectId


REQUEST_HEADERS = {
    'Accept': "application/json",
    'Content-Type': "application/json",
}
RESPONSE_HEADERS = {
    'Accept': "application/json",
}


class TestGrantController(BaseTestCase):
    """GrantController integration test stubs"""

    def setUp(self):
        util.connect_db()
        DbGrant.objects().delete()

    def tearDown(self):
        util.disconnect_db()

    def test_create_grant_with_status201(self):
        """Test case for create_grant

        Create a new grant (201)
        """
        grant = {
            'name': "awesome-grant",
            'description': "description",
            'url': "https://report.nih.gov/"
        }
        response = self.client.open(
            "/api/v1/grants",
            method="POST",
            headers=REQUEST_HEADERS,
            data=json.dumps(grant),
            content_type="application/json"
        )
        self.assert_status(
            response, 201,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_create_grant_with_status400(self):
        """Test case for create_grant

        Create an empty grant (400)
        """
        grant = {}
        response = self.client.open(
            "/api/v1/grants",
            method="POST",
            headers=REQUEST_HEADERS,
            data=json.dumps(grant),
            content_type="application/json"
        )
        self.assert_400(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    # TODO: update controller so that NotUniqueError is thrown
    # def test_create_grant_with_status409(self):
    #     """Test case for create_grant

    #     Create a duplicate grant (409)
    #     """
    #     grant = util.create_test_grant()
    #     dup_grant = {
    #         'name': "awesome-grant",
    #         'description': "description",
    #         'url': "https://report.nih.gov/"
    #     }
    #     response = self.client.open(
    #         "/api/v1/grants",
    #         method="POST",
    #         headers=REQUEST_HEADERS,
    #         data=json.dumps(dup_grant),
    #         content_type="application/json"
    #     )
    #     with self.assertRaises(NotUniqueError):
    #         self.assert_status(
    #             response, 409,
    #             f"Response body is: {response.data.decode('utf-8')}"
    #         )

    def test_delete_grant_with_status200(self):
        """Test case for delete_grant

        Delete an existing grant (200)
        """
        grant = util.create_test_grant()
        response = self.client.open(
            f"/api/v1/grants/{grant.grantId}",
            method="DELETE",
            headers=RESPONSE_HEADERS
        )
        self.assert_200(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_delete_grant_with_status404(self):
        """Test case for delete_grant

        Delete an unknown grant (404)
        """
        grant_id = ObjectId()
        response = self.client.open(
            f"/api/v1/grants/{grant_id}",
            method="DELETE",
            headers=RESPONSE_HEADERS
        )
        self.assert_404(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_get_grant_with_status200(self):
        """Test case for get_grant

        Get an existing grant (200)
        """
        grant = util.create_test_grant()
        response = self.client.open(
            f"/api/v1/grants/{grant.grantId}",
            method="GET",
            headers=RESPONSE_HEADERS
        )
        self.assert_200(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_get_grant_with_status404(self):
        """Test case for get_grant

        Get an unknown grant (404)
        """
        grant_id = ObjectId()
        response = self.client.open(
            f"/api/v1/grants/{grant_id}",
            method="GET",
            headers=RESPONSE_HEADERS
        )
        self.assert_404(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_list_grants_with_status200(self):
        """Test case for list_grants

        Get all grants (200)
        """
        util.create_test_grant()
        query_string = [("limit", 10),
                        ("offset", 0)]
        response = self.client.open(
            "/api/v1/grants",
            method="GET",
            headers=RESPONSE_HEADERS,
            query_string=query_string
        )
        self.assert_200(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_list_grants_with_status400(self):
        """Test case for list_grants

        Get all grants using an invalid query (400)
        """
        util.create_test_grant()
        query_string = [("limit", "no-limit"),
                        ("offset", "none")]
        response = self.client.open(
            "/api/v1/grants",
            method="GET",
            headers=RESPONSE_HEADERS,
            query_string=query_string
        )
        self.assert_400(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )


if __name__ == "__main__":
    unittest.main()
