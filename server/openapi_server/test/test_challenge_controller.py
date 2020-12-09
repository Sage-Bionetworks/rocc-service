# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
# from six import BytesIO

# from openapi_server.models.challenge import Challenge  # noqa: E501
# from openapi_server.models.error import Error  # noqa: E501
# from openapi_server.models.page_of_challenges import PageOfChallenges  # noqa: E501
from openapi_server.test import BaseTestCase


class TestChallengeController(BaseTestCase):
    """ChallengeController integration test stubs"""

    def disabled_test_create_challenge(self):
        """Test case for create_challenge

        Add a challenge
        """
        challenge = {
            "url": "https://synapse.org/sample-challenge",
            "endDate": "2020-12-31",
            "name": "Sample Challenge",
            "organizers": [{
                "firstName": "John",
                "lastName": "Smith",
                "id": "507f1f77bcf86cd799439011",
                "email": "john.smith@example.com"
            }, {
                "firstName": "Jane",
                "lastName": "Smith",
                "id": "507f1f77bcf86cd799439011",
                "email": "jane.smith@example.com"
            }],
            "grant": [{
                "sponsor": {
                    "name": "Sage Bionetworks",
                    "id": "507f1f77bcf86cd799439011",
                    "url": "https://sagebionetworks.org/"
                },
                "name": "name",
                "description": "description",
                "id": "507f1f77bcf86cd799439011",
                "url": "https://openapi-generator.tech"
            }],
            "startDate": "2020-11-10",
            "status": "open",
            "tags": ["Machine Learning", "Breast Cancer"]
        }
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/challenges',
            method='POST',
            headers=headers,
            data=json.dumps(challenge),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def disabled_test_delete_challenge(self):
        """Test case for delete_challenge

        Delete a challenge
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/challenges/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def disabled_test_get_challenge(self):
        """Test case for get_challenge

        Get a challenge
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/challenges/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def disabled_test_list_challenges(self):
        """Test case for list_challenges

        List all the challenges
        """
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/challenges',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
