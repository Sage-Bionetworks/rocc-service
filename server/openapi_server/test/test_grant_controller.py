# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.grant import Grant  # noqa: E501
from openapi_server.models.page_of_grants import PageOfGrants  # noqa: E501
from openapi_server.test import BaseTestCase


class TestGrantController(BaseTestCase):
    """GrantController integration test stubs"""

    def test_create_grant(self):
        """Test case for create_grant

        Create a grant
        """
        grant = {
  "grantId" : "507f1f77bcf86cd799439011",
  "name" : "name",
  "description" : "description",
  "url" : "https://openapi-generator.tech"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/grants',
            method='POST',
            headers=headers,
            data=json.dumps(grant),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_grant(self):
        """Test case for delete_grant

        Delete a grant
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/grants/{grant_id}'.format(grant_id='grant_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_grant(self):
        """Test case for get_grant

        Get a grant
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/grants/{grant_id}'.format(grant_id='grant_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_grants(self):
        """Test case for list_grants

        Get all grants
        """
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/grants',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
