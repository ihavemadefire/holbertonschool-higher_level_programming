class Node:
    """Thie class defines the structure of a singly linked list node"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Recreates a sll head double pointer"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data >value:
            new.next_node = self.__head
            self.__head = new
        else:
            c = self.__head
            while c.next_node is not None and c.next_node.data < value:
                c = c.next_node
            new.next_node = c.next_node
            c.next_node = new

    def __str__(self):
        ret = []
        temp = self.__head
        while temp is not None:
            ret.append(str(temp.data))
            temp = temp.next_node
        final = '\n'.join(ret)
        return final
