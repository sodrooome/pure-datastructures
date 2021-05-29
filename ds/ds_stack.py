from typing import Optional, List
from .exception import DsIndexError, DsPeekIndexError


class Stack:
    def __init__(self, maxsize: int = 10) -> None:
        """
        Initialize stack. params:
        :items: array and empty
        :maxsize: size of array
        :top: integer
        """
        self.items: int = []
        self.top: int = 0
        self.array: List[int] = [] * maxsize

    def __iter__(self):
        probe = self.top
        while True:
            if probe == -1:
                return
            yield self.array[probe]
            probe = probe - 1

    def __str__(self):
        result = " ".join(map(str, self))
        return "Top - " + result

    def __bool__(self):
        if self.items > 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self.items) > 1:
            return True
        else:
            return False

    def is_empty(self):
        if self.top < 1:
            return True
        else:
            return False

    def procedure_push(self, item):
        self.top = self.top + 1
        if self.top == len(self.array):
            self.expand_size()
        self.array[self.top] = item

    def procedure_pop(self):
        if self.is_empty():
            raise DsIndexError()
        item = self.array[self.top]
        self.top = self.top - 1
        return item

    def procedure_peek(self):
        """Check the top-most element of the stack."""
        if self.is_empty():
            raise DsIndexError()
        return self.array[self.top]

    def procedure_expand_size(self):
        """Expands size of the stack using : 0(n)"""
        return len(self.array)


class Node:
    """
    Representing node, params:
    :data: data -> Any
    :next: frame or None
    """

    def __init__(self, data):
        self.data = data
        self.next: Optional[str] = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        # super().__init__()
        self.head: Optional[str] = None
        self.top: int = 0

    def __iter__(self):
        probe = self.head
        while True:
            if probe is None:
                return
            yield probe.data
            probe = probe.next

    def is_full(self):
        if len(self.top) > 1:
            return True
        else:
            return False

    def is_empty(self):
        if self.top < 1:
            return True
        else:
            return False

    def procedure_push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.top = self.top + 1

    def procedure_pop(self):
        if self.is_empty():
            raise DsIndexError()
        data = self.head.data
        self.head = self.head.next
        self.top = self.top - 1
        return data

    def procedure_peek(self):
        if self.is_empty():
            raise DsPeekIndexError()
        return self.head.data


# Got some error, list shouldn't be have an object
class OrderedStack:
    def __init__(self):
        self.items: List[int] = []

    def is_empty(self):
        return self.items == []

    def procedure_push(self, item):
        self.items.procedure_push(item)

    def procedure_pop(self):
        stack = Stack()
        if self.is_empty():
            raise DsIndexError()
        return self.items.stack.procedure_pop()
