#!/usr/bin/python3
"""Unittests for Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

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

class TestRectangleClass(unittest.TestCase):
    """Basic tests for the rectangle class"""

    def test_normal(self):
        """Two passed arguments"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 4)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

    def test_optionals(self):
        """5 passed arguments"""
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 12)

    def test_errors1(self):
        """Tests for no args"""
        self.assertRaises(ExpectedException, Rectangle)

if __name__ == '__main__':
    unittest.main()
