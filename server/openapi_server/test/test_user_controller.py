# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.user import User  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_get_user_by_name(self):
        """Test case for get_user_by_name

        Get user by user name
        """
        query_string = [('pretty_print', True),
                        ('with_email', True)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/users/{username}'.format(username='username_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consummes. See https://github.com/zalando/connexion/pull/760")
    def test_update_user(self):
        """Test case for update_user

        Updated user
        """
        user = {
  "firstName" : "John",
  "lastName" : "Smith",
  "email" : "john.smith@example.com",
  "username" : "John78"
}
        query_string = [('pretty_print', True)]
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/users/{username}'.format(username='username_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(user),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
