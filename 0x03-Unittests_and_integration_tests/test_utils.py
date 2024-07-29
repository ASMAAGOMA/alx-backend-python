#!/usr/bin/env python3
"""
test for access_nested_map
"""


import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),

    ])
    def test_access_nested_map_exception(self, nested_map, path, message):
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual(str(err.exception), message)


class TestGetJson(unittest.TestCase):  

    @parameterized.expand([  
        ("http://example.com", {"payload": True}),  
        ("http://holberton.io", {"payload": False}),  
    ])  
    @patch('utils.requests.get')  
    def test_get_json(self, test_url, test_payload, mock_get):  
        mock_response = Mock()  
        mock_response.json.return_value = test_payload  
        mock_get.return_value = mock_response  
        
        result = get_json(test_url)  

        mock_get.assert_called_once_with(test_url)  
        self.assertEqual(result, test_payload)  


if __name__ == '__main__':
    unittest.main()