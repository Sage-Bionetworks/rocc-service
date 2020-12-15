# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json

from openapi_server.dbmodels.organization import Organization as DbOrganization  # noqa: E501
from openapi_server.test.integration import BaseTestCase
from openapi_server.test.integration import util


class TestOrganizationController(BaseTestCase):
    """OrganizationController integration test stubs"""

    def setUp(self):
        util.connect_db()
        DbOrganization.objects().delete()

    def tearDown(self):
        util.disconnect_db()

    def test_create_organization(self):
        """Test case for create_organization

        Create an organization
        """
        organization = {
            "organizationId": "awesome-organization",
            "name": "name",
            "shortName": "shortName",
            "url": "https://openapi-generator.tech"
        }
        query_string = [('organizationId', 'awesome-organization')]
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/organizations',
            method='POST',
            headers=headers,
            data=json.dumps(organization),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_organization(self):
        """Test case for delete_organization

        Delete an organization
        """
        util.create_test_organization("sage-bionetworks")
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/organizations/{organization_id}'.format(
                organization_id='sage-bionetworks'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_organization(self):
        """Test case for get_organization

        Get an organization
        """
        util.create_test_organization("sage-bionetworks")
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/organizations/{organization_id}'.format(
                organization_id='sage-bionetworks'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_organizations(self):
        """Test case for list_organizations

        Get all organizations
        """
        util.create_test_organization("sage-bionetworks")
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/organizations',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
