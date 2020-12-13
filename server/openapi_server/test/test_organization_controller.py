# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.organization import Organization  # noqa: E501
from openapi_server.models.page_of_organizations import PageOfOrganizations  # noqa: E501
from openapi_server.test import BaseTestCase


class TestOrganizationController(BaseTestCase):
    """OrganizationController integration test stubs"""

    def test_create_organization(self):
        """Test case for create_organization

        Create an organization
        """
        organization = {
  "organizationId" : "awesome-organization",
  "name" : "name",
  "shortName" : "shortName",
  "url" : "https://openapi-generator.tech"
}
        query_string = [('organizationId', 'organization_id_example')]
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
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/organizations/{organization_id}'.format(organization_id='organization_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_organization(self):
        """Test case for get_organization

        Get an organization
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/organizations/{organization_id}'.format(organization_id='organization_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_organizations(self):
        """Test case for list_organizations

        Get all organizations
        """
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
