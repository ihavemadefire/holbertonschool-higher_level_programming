#!/usr/bin/python3
"""Unittests for max int problem"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test defs for max integer"""

    def test_normal_list(self):
        """Normal ordered list"""
        list = [6, 7, 8, 9]
        self.assertEqual(max_integer(list), 9)

    def test_unordered_list(self):
        """Normal unordered list"""
        list = [6, 9, 8, 7]
        self.assertEqual(max_integer(list), 9)

    def test_max1_list(self):
        """Normal ordered list"""
        list = [9, 7, 8, 4]
        self.assertEqual(max_integer(list), 9)

    def test_empty_list(self):
        """Empty list"""
        list = []
        self.assertEqual(max_integer(list), None)

    def test_single_list(self):
        """Single list"""
        list = [9]
        self.assertEqual(max_integer(list), 9)

    def test_negative1_list(self):
        """Normal ordered list"""
        list = [6, -7, 8, 9]
        self.assertEqual(max_integer(list), 9)

    def test_negativeall_list(self):
        """Normal ordered list"""
        list = [-6, -7, -8, -9]
        self.assertEqual(max_integer(list), -6)

if __name__ == '__main__':
    unittest.main()
