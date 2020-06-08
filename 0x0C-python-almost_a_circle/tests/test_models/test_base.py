#!/usr/bin/python3
"""Unittests for Base class"""
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    """Test defs for base class"""

    def test_normal(self):
        """Normal ordered list"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_normal_inc(self):
        """Normal ordered list"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 3)

    def test_normal_add_id(self):
        """Normal ordered list"""
        b1 = Base(42)
        self.assertEqual(b1.id, 42)

if __name__ == '__main__':
    unittest.main()
