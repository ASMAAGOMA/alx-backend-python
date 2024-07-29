#!/usr/bin/env python3
"""
test for access_nested_map
"""


import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


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


class TestMemoize(unittest.TestCase):
    """ test class to tes utils.memoize"""

    def test_memoize(self):
        """ Tests the function when calling a_property twice,
        the correct result is returned but a_method is only
        called once using assert_called_once
        """

        class TestClass:
            """ Test Class for wrapping with memoize """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
