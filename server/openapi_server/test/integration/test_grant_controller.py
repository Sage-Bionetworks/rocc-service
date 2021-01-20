# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json

from openapi_server.dbmodels.grant import Grant as DbGrant
from openapi_server.test.integration import BaseTestCase
from openapi_server.test.integration import util


class TestGrantController(BaseTestCase):
    """GrantController integration test stubs"""

    def setUp(self):
        util.connect_db()
        DbGrant.objects().delete()

    def tearDown(self):
        util.disconnect_db()

    def test_create_grant(self):
        """Test case for create_grant

        Create a grant
        """
        grant = {
            'name': "awesome-grant",
            'description': "description",
            'url': "https://report.nih.gov/"
        }
        headers = {
            'Accept': "application/json",
            'Content-Type': "application/json",
        }
        response = self.client.open(
            "/api/v1/grants",
            method="POST",
            headers=headers,
            data=json.dumps(grant),
            content_type="application/json"
        )
        self.assert_status(
            response, 201,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_delete_grant(self):
        """Test case for delete_grant

        Delete a grant
        """
        grant = util.create_test_grant()
        headers = {
            'Accept': "application/json",
        }
        response = self.client.open(
            f"/api/v1/grants/{grant.grantId}",
            method="DELETE",
            headers=headers
        )
        self.assert200(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_get_grant(self):
        """Test case for get_grant

        Get a grant
        """
        grant = util.create_test_grant()
        headers = {
            'Accept': "application/json",
        }
        response = self.client.open(
            f"/api/v1/grants/{grant.grantId}",
            method="GET",
            headers=headers
        )
        self.assert200(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_list_grants(self):
        """Test case for list_grants

        Get all grants
        """
        util.create_test_grant()
        query_string = [("limit", 10),
                        ("offset", 0)]
        headers = {
            'Accept': "application/json",
        }
        response = self.client.open(
            "/api/v1/grants",
            method="GET",
            headers=headers,
            query_string=query_string
        )
        self.assert200(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )


if __name__ == "__main__":
    unittest.main()
