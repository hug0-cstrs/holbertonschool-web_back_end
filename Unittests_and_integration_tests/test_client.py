#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        expected_result = {"name": org_name}
        mock_get_json.return_value = expected_result

        github_client = GithubOrgClient(org_name)
        result = github_client.org()

        self.assertEqual(result, expected_result)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")


if __name__ == '__main__':
    unittest.main()
