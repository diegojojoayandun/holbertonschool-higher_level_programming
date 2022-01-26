#!/usr/bin/python3
"""Unittest for the max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_regular(self):
        """regular test with list of ints"""
        l = [2, 4, 6, 8, 10]
        result = max_integer(l)
        self.assertEqual(result, 10)

    def test_non_int(self):
        """non integers Test:
        raise a TypeError exception"""
        l = ["x", "y", 10]
        self.assertRaises(TypeError, max_integer, l)

    def test_empty_list(self):
        """empty list test: return None"""
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def test_negative_values(self):
        """negative values test: return the max"""
        l = [-3, -2, -1]
        result = max_integer(l)
        self.assertEqual(result, -1)

    def test_float_int_values(self):
        """float and int values test: return the max"""
        l = [1, 2, 3, 4, 5.5, 6]
        result = max_integer(l)
        self.assertEqual(result, 6)

    def test_not_list(self):
        """not a list test: raise a TypeError"""
        self.assertRaises(TypeError, max_integer, 1)

    def test_only_value(self):
        """only one value test: return the same value"""
        l = [5]
        result = max_integer(l)
        self.assertEqual(result, 5)

    def test__all_same_value(self):
        """the same values test: return the value"""
        l = [5, 5, 5, 5, 5]
        result = max_integer(l)
        self.assertEqual(result, 5)

    def test_strings(self):
        """list of strings test: return the first string"""
        l = ["hello", "World"]
        result = max_integer(l)
        self.assertEqual(result, "hello")

    def test_none(self):
        """None as parameter test: raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)


if __name__ == '__main__':
    unittest.main()
