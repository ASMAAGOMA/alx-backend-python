#!/usr/bin/env python3
"""
test for access_nested_map
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a"), "key not found: a"),
        ({"a": 1}, ("a", "b"), "key not found: b"),

    ])
    def test_access_nested_map_exception(self, nestes_map, path, message):
        with self.assertRaises(KeyError) as err:
            access_nested_map(nestes_map, path)
        self.assertEqual(str(err.exception), message)

if __name__ == '__main__':
    unittest.main()