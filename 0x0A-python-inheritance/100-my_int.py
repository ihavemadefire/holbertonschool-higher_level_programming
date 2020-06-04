#!/usr/bin/python3
"""Docstring"""


class MyInt(int):
    """Docstring"""
    def __eq__(self, other):
        """Docstring"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Docstring"""
        return super().__eq__(other)
