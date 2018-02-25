"""
Linked List Data Structure.
"""


class ListNode:
    """
    Class represents Node of singly-linked list.
    """
    def __init__(self, data, next=None):
        self._data = data
        self._next = next

    def _get_data(self):
        return self._data

    def _set_data(self, new_data):
        self._data = new_data

    def _get_next(self):
        return self._next

    def _set_next(self, new_next):
        self._next = new_next

    data = property(_get_data, _set_data)
    next = property(_get_next, _set_next)

    def __repr__(self):
        return repr(self._data)


class SinglyLinkedList:
    """
    Class represents singly-linked list data structure.
    """
    def __init__(self):
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head

        while curr:
            nodes.append(repr(curr))
            curr = curr.next

        return 'LinkedList <[' + ', '.join(nodes) + ']>'

    def is_empty(self):
        return self.head is None

    def prepend(self, item):
        """
        Insert new item at the beginning of the list.
        """
        self.head = ListNode(data=item, next=self.head)

    def append(self, item):
        """
        Add new item to the end of the list.
        """
        if self.is_empty():
            self.head = ListNode(data=item)
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = ListNode(data=item)

    def find(self, element):
        """
        Stupid method???

        Search for the first element with `data` matching `element`.
        Takes O(n) time.

        :param element: element to find.
        :return: the element or `None` if not found.
        """
        curr = self.head

        while curr and curr.data != element:
            curr = curr.next

        return curr  # Will be None if not found

    def remove(self, element):
        """
        Remove the first occurrence of `element` in the list.
        Takes O(n) time.
        """
        # Find the element and keep a reference to the element preceding it
        curr = self.head
        prev = None

        while curr and curr.data != element:
            prev = curr
            curr = curr.next
        # Unlink it from the list
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None  # ???

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev_node = None
        next_node = None

        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node

        self.head = prev_node

# ======================================================================


class DListNode:
    """
    Class represents Node of a doubly-linked list.
    """
    def __init__(self, data=None, prev=None, next=None):
        self._data = data
        self._prev = prev
        self._next = next

    def _get_data(self):
        return self._data

    def _set_data(self, new_data):
        self._data = new_data

    def _get_prev(self):
        return self._prev

    def _set_prev(self, new_prev):
        self._prev = new_prev

    def _get_next(self):
        return self._next

    def _set_next(self, new_next):
        self._next = new_next

    data = property(_get_data, _set_data)
    prev = property(_get_prev, _set_prev)
    next = property(_get_next, _set_next)

    def __repr__(self):
        return repr(self.data)


class DoublyLinkedList:
    """
    Class represents doubly-linked list data structure.
    """
    def __init__(self):
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head

        while curr:
            nodes.append(repr(curr))
            curr = curr.next

        return 'DoublyLinkedList <[' + ', '.join(nodes) + ']>'

    def prepend(self, data):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        new_head = DListNode(data=data, next=self.head)

        if self.head:
            self.head.prev = new_head

        self.head = new_head

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:
            self.head = DListNode(data=data)
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = DListNode(data=data, prev=curr)

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head

        while curr and curr.data != key:
            curr = curr.next

        return curr  # Will be None if not found

    def remove_node(self, node):
        """
        Unlink node from the list.
        Takes O(1) time.
        """
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if node is self.head:
            self.head = node.next

        node.prev = None
        node.next = None

    def remove_element(self, element):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        node = self.find(element)

        if not node:
            return

        self.remove_node(node)

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev_node = None

        while curr:
            prev_node = curr.prev
            curr.prev = curr.next
            curr.next = prev_node
            curr = curr.prev

        self.head = prev_node.prev
