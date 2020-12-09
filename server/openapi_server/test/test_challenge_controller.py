# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json

from openapi_server.dbmodels.challenge import Challenge as DbChallenge
from openapi_server.test import BaseTestCase
from openapi_server.test import util


class TestChallengeController(BaseTestCase):
    """ChallengeController integration test stubs"""

    def setUp(self):
        util.connect_db()
        DbChallenge.objects().delete()

    def tearDown(self):
        util.disconnect_db()

    def disabled_test_create_challenge(self):
        """Test case for create_challenge

        Add a challenge
        """
        challenge = {
            "name": "Sample Challenge",
            "startDate": "2020-11-10",
            "endDate": "2020-12-31",
            "url": "https://synapse.org/sample-challenge",
            "status": "open",
            "organizers": [{
                "firstName": "John",
                "lastName": "Smith",
                "email": "john.smith@example.com"
            }],
            "organizations": [{
                "name": "Sage Bionetworks",
                "url": "https://www.sagebionetworks.org"
            }],
            "grant": [],
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

    def test_get_challenge(self):
        """Test case for get_challenge

        Get a challenge
        """
        util.create_test_challenge("awesome-challenge")
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/challenges/{id}'.format(id='awesome-challenge'),
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
