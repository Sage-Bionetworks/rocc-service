# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json

from openapi_server.dbmodels.organization import Organization as DbOrganization
from openapi_server.dbmodels.person import Person as DbPerson
from openapi_server.test.integration import BaseTestCase
from openapi_server.test.integration import util


class TestPersonController(BaseTestCase):
    """PersonController integration test stubs"""

    def setUp(self):
        util.connect_db()
        DbOrganization.objects().delete()
        DbPerson.objects().delete()
        util.create_test_organization('awesome-organization')

    def tearDown(self):
        util.disconnect_db()

    def test_create_person(self):
        """Test case for create_person

        Create a person
        """
        person = {
            "firstName": "John",
            "lastName": "Smith",
            "organizations": ["awesome-organization"],
            "email": "john.smith@example.com"
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
        person = util.create_test_person(
            organizations=['awesome-organization'])
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/persons/{person_id}'.format(person_id=person.personId),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_person(self):
        """Test case for get_person

        Get a person
        """
        person = util.create_test_person(
            organizations=['awesome-organization'])
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/persons/{person_id}'.format(person_id=person.personId),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_persons(self):
        """Test case for list_persons

        Get all persons
        """
        util.create_test_person(
            organizations=['awesome-organization'])
        query_string = [('limit', 10),
                        ('offset', 0),
                        ('filter_', {
                            # TODO: add values to increase coverage
                        })]
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
