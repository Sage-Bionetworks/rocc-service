# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from bson.objectid import ObjectId

from openapi_server.dbmodels.tag import Tag as DbTag
# from openapi_server.models.tag_filter import TagFilter
from openapi_server.test.integration import BaseTestCase
from openapi_server.test.integration import util


ID_QUERY = [("tagId", "awesome-tag")]
REQUEST_HEADERS = {
    'Accept': "application/json",
    'Content-Type': "application/json",
}
RESPONSE_HEADERS = {
    'Accept': "application/json",
}

# TODO: mock 500 reponses


class TestTagController(BaseTestCase):
    """TagController integration test stubs"""

    def setUp(self):
        util.connect_db()
        DbTag.objects().delete()

    def tearDown(self):
        util.disconnect_db()

    def test_create_tag_with_status201(self):
        """Test case for create_tag

        Create a tag (200)
        """
        tag = {
            'description': "description"
        }
        response = self.client.open(
            "/api/v1/tags",
            method="POST",
            headers=REQUEST_HEADERS,
            data=json.dumps(tag),
            content_type="application/json",
            query_string=ID_QUERY)
        self.assertStatus(
            response, 201,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_create_tag_with_status400(self):
        """Test case for create_tag

        Create a (non-JSON) tag (400)
        """
        tag = {
            'description': "description"
        }
        response = self.client.open(
            "/api/v1/tags",
            method="POST",
            headers=REQUEST_HEADERS,
            data=tag,
            content_type="application/json",
            query_string=ID_QUERY)
        self.assert400(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_create_tag_with_status409(self):
        """Test case for create_tag

        Create a duplicate tag (409)
        """
        util.create_test_tag("awesome-tag")  # duplicated Tag
        tag = {
            'description': "description"
        }
        response = self.client.open(
            "/api/v1/tags",
            method="POST",
            headers=REQUEST_HEADERS,
            data=json.dumps(tag),
            content_type="application/json",
            query_string=ID_QUERY)
        self.assertStatus(
            response, 409,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_delete_tag_with_status200(self):
        """Test case for delete_tag

        Delete an existing tag (200)
        """
        tag = util.create_test_tag("awesome-tag")
        response = self.client.open(
            f"/api/v1/tags/{tag.tagId}",
            method="DELETE",
            headers=RESPONSE_HEADERS)
        self.assert200(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_delete_tag_with_status404(self):
        """Test case for delete_tag

        Delete an unknown tag (404)
        """
        tag_id = ObjectId()
        response = self.client.open(
            f"/api/v1/tags/{tag_id}",
            method="DELETE",
            headers=RESPONSE_HEADERS)
        self.assert404(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_get_tag_with_status200(self):
        """Test case for get_tag

        Get an existing tag (200)
        """
        tag = util.create_test_tag("awesome-tag")
        response = self.client.open(
            f"/api/v1/tags/{tag.tagId}",
            method="GET",
            headers=RESPONSE_HEADERS)
        self.assert200(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_get_tag_with_status404(self):
        """Test case for get_tag

        Get an unknown tag (404)
        """
        tag_id = ObjectId()
        response = self.client.open(
            f"/api/v1/tags/{tag_id}",
            method="GET",
            headers=RESPONSE_HEADERS)
        self.assert404(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_list_tags_with_status200(self):
        """Test case for list_tags

        Get all tags (200)
        """
        util.create_test_tag("awesome-tag")
        query_string = [("limit", 10),
                        ("offset", 0),
                        ("filter_", {
                            # TODO: add values to increase coverage
                        })]
        response = self.client.open(
            "/api/v1/tags",
            method="GET",
            headers=RESPONSE_HEADERS,
            query_string=query_string)
        self.assert200(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )

    def test_list_tags_with_status400(self):
        """Test case for list_tags

        Get all tags using an invalid query (400)
        """
        util.create_test_tag("awesome-tag")
        query_string = [("limit", "no-limit"),
                        ("offset", "none"),
                        ("filter_", {
                            # TODO: add values to increase coverage
                        })]
        response = self.client.open(
            "/api/v1/tags",
            method="GET",
            headers=RESPONSE_HEADERS,
            query_string=query_string)
        self.assert400(
            response,
            f"Response body is: {response.data.decode('utf-8')}"
        )


if __name__ == "__main__":
    unittest.main()
