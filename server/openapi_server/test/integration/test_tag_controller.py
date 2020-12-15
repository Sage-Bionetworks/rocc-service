# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json

# from openapi_server.dbmodels.tag import Tag as DbTag # noqa: E501
# from openapi_server.models.error import Error  # noqa: E501
# from openapi_server.models.page_of_tags import PageOfTags  # noqa: E501
# from openapi_server.models.tag import Tag  # noqa: E501
from openapi_server.test.integration import BaseTestCase
from openapi_server.test.integration import util


class TestTagController(BaseTestCase):
    """TagController integration test stubs"""

    def setUp(self):
        util.connect_db()
        # DbTag.objects().delete()

    def tearDown(self):
        util.disconnect_db()

    def test_create_tag(self):
        """Test case for create_tag

        Create a tag
        """
        tag = {
            "description": "description"
        }
        query_string = [('tagId', 'awesome-tag')]
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/tags',
            method='POST',
            headers=headers,
            data=json.dumps(tag),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def delete_tag(self):
        """Test case for delete_tag

        Delete a tag
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/tags/{tag_id}'.format(tag_id='tag_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def get_tag(self):
        """Test case for get_tag

        Get a tag
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/tags/{tag_id}'.format(tag_id='tag_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def list_tags(self):
        """Test case for list_tags

        Get all tags
        """
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/tags',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
