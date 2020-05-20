#!/usr/bin/python3
"""Defines node and linked list head."""


class Node:
    """This class defines the structure of a singly linked list node."""
    def __init__(self, data, next_node=None):
        """Init a new instance of Square given a size.
        Args:
            data (int): Size of one side of the square.
            next_node (Node): Link to next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter and setter for node data."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter and setter for next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Recreates a sll head double pointer."""

    def __init__(self):
        """Inits a new list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts new node.
        Args:
            value (Node): node to be inserted.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            c = self.__head
            while c.next_node is not None and c.next_node.data < value:
                c = c.next_node
            new.next_node = c.next_node
            c.next_node = new

    def __str__(self):
        """Generates string representation for printing."""
        ret = []
        temp = self.__head
        while temp is not None:
            ret.append(str(temp.data))
            temp = temp.next_node
        final = '\n'.join(ret)
        return final
