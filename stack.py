"""
Stack Data Structure
"""

from collections import deque


class StackError(Exception):
    pass


class Stack:
    """
    Class represents stack data structure.

    Available operations:
    push - put element on top of stack
    pop - remove element from the top of stack
    peek - return top of stack (w/o removing it)
    is_empty - check whether stack have no items
    is_full - check whether stack is full (if size is provided)
    """

    def __init__(self, size=None):
        self._stack = deque(maxlen=size)

    def push(self, item):
        # TODO: implement push multiple items e.g. s.push(1,2,3)
        if self.is_full():
            raise StackError('Stack Overflow!')
        self._stack.append(item)

    def pop(self):
        if self.is_empty():
            raise StackError('Stack Underflow!')

        return self._stack.pop()

    def peek(self):
        return self._stack[-1]

    def is_empty(self):
        return len(self) == 0

    def is_full(self):
        return self._stack.maxlen == len(self)

    def __len__(self):
        return len(self._stack)
