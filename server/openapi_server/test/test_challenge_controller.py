# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.challenge import Challenge  # noqa: E501
from openapi_server.test import BaseTestCase


class TestChallengeController(BaseTestCase):
    """ChallengeController integration test stubs"""

    def test_challenges_read(self):
        """Test case for challenges_read

        Get a challenge by ID
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

    def test_challenges_update(self):
        """Test case for challenges_update

        Update a challenge by ID
        """
        challenge = {
  "title" : "title"
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/challenges/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(challenge),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_notes_read_all(self):
        """Test case for notes_read_all

        Get all challenges
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/challenges',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
