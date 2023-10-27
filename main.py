
class ListError(ValueError):
    """"Class for generate custom ListError"""
    def __init__(self, message):
        super().__init__(message)


class Node:
    """General Node-Class"""

    def __init__(self, data):
        self.data = data
        self._prev = None
        self._next = None


class DoubleLinkedList:
    """General Double Link-Class"""
    def __init__(self):
        self.head = None

    def push_in_empty(self, data):
        # Insert new Node in start List if is empty
        if self.head is None:
            self.head = Node(data)
        else:
            raise ListError('List is not empty')

    def push_front(self, data):
        # Insert a new Node in List on front
        if self.head is None:
            self.push_in_empty(data)
            return
        new_node = Node(data)
        new_node._next = self.head
        self.head._prev = new_node
        self.head = new_node

    def push_back(self, data):
        # insert a new Node in List on back
        if self.head is None:
            self.push_in_empty(data)
            return
        current = self.head
        while current._next:
            current = current._next
        new_node = Node(data)
        current._next = new_node
        new_node._prev = current

    def push_after(self, node_content, data):
        # Insert a new Node after existing Node
        if self.head is None:
            raise ListError('List is empty')
        current = self.head
        while current:
            if current.data == node_content:
                new_node = Node(data)
                new_node._prev, new_node._next = current, current._next
                if current._next:
                    current._next._prev = new_node
                current._next = new_node
                return
            current = current._next
        raise ListError('Item not in the list')

    def push_before(self, node_content, data):
        # Insert a new Node before an existing Node
        if self.head is None:
            raise ListError('List is empty')
        current = self.head
        while current:
            if current.data == node_content:
                new_node = Node(data)
                new_node._next, new_node._prev = current, current._prev
                if current._prev:
                    current._prev._next = new_node
                else:
                    self.head = new_node
                current._prev = new_node
                return
            current = current._next
        raise ListError('Item not in the list')

    def travers_linked_list(self):
        # Travers all Nodes from Linked List
        data_list = []
        current = self.head
        while current:
            data_list.append(current.data)
            current = current._next
        return data_list

    def reverse_linked_list(self):
        # Revers all Nodes in list
        current = self.head
        while current:
            current._prev, current._next = current._next, current._prev
            self.head = current
            current = current._prev

    def delete_node_by_value(self, node_content):
        # Delete Node by Node-Value
        current = self.head
        while current:
            if current.data == node_content:
                if current._prev:
                    current._prev._next = current._next
                else:
                    self.head = current._next
                if current._next:
                    current._next._prev = current._prev
                return
            current = current._next
        raise ListError('Element not found')


# TESTS

import unittest


class TestDoubleLinkedList(unittest.TestCase):
    def setUp(self):
        self.my_list = DoubleLinkedList()

    def test_push_in_empty(self):
        self.my_list.push_in_empty(1)
        self.assertEqual(self.my_list.travers_linked_list(), [1])

    def test_push_front(self):
        self.my_list.push_front(2)
        self.my_list.push_front(1)
        self.assertEqual(self.my_list.travers_linked_list(), [1, 2])

    def test_push_back(self):
        self.my_list.push_back(1)
        self.my_list.push_back(2)
        self.assertEqual(self.my_list.travers_linked_list(), [1, 2])

    def test_push_after(self):
        self.my_list.push_back(1)
        self.my_list.push_after(1, 2)
        self.assertEqual(self.my_list.travers_linked_list(), [1, 2])

    def test_push_before(self):
        self.my_list.push_back(1)
        self.my_list.push_before(1, 2)
        self.assertEqual(self.my_list.travers_linked_list(), [2, 1])

    def test_reverse_linked_list(self):
        self.my_list.push_back(1)
        self.my_list.push_back(2)
        self.my_list.reverse_linked_list()
        self.assertEqual(self.my_list.travers_linked_list(), [2, 1])

    def test_delete_node_by_value(self):
        self.my_list.push_back(1)
        self.my_list.push_back(2)
        self.my_list.delete_node_by_value(2)
        self.assertEqual(self.my_list.travers_linked_list(), [1])


if __name__ == '__main__':
    unittest.main()
