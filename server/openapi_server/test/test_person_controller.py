# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_persons import PageOfPersons  # noqa: E501
from openapi_server.models.person import Person  # noqa: E501
from openapi_server.test import BaseTestCase


class TestPersonController(BaseTestCase):
    """PersonController integration test stubs"""

    def test_create_person(self):
        """Test case for create_person

        Create a person
        """
        person = {
  "firstName" : "John",
  "lastName" : "Smith",
  "organizations" : [ "awesome-organization", "awesome-organization" ],
  "personId" : "",
  "email" : "john.smith@example.com"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/persons',
            method='POST',
            headers=headers,
            data=json.dumps(person),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_person(self):
        """Test case for delete_person

        Delete a person
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/persons/{person_id}'.format(person_id='person_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_person(self):
        """Test case for get_person

        Get a person
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/persons/{person_id}'.format(person_id='person_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_persons(self):
        """Test case for list_persons

        Get all persons
        """
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/persons',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
