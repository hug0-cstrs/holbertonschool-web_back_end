#!/usr/bin/env python3
"""Unittests for utils.py"""
import unittest
from unittest.mock import Mock, patch

from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test access_nested_map with exception """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """ Class for Testing Get Json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test that utils.get_json returns the expected result."""
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()


class TestMemoize(unittest.TestCase):
    """ Class for Testing"""

    def test_memoize(self):
        """ Test that memoize behaves as expected """

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                """A property that memoizes a_method"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock_method.assert_called_once()
