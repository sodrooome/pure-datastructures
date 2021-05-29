from typing import Optional
from .exception import DsIndexError, DsPeekIndexError


class Queue:
    def __init__(self, maxsize: int = 10) -> int:
        """
        Initialize Queue. params:
        :size: Array and empty
        :front: integers and null
        :rear: integers and null
        :value: integers and null
        """
        self.front: int = 0
        self.rear: int = 0
        self.value: int = 0
        self.size = [None] * maxsize

    def __bool__(self):
        if len(self.size) > 0:
            return True
        else:
            return False

    def is_empty(self):
        """Check queue is Empty or not"""
        if self.value < 1:
            return True
        else:
            return False

    def is_full(self):
        """Check queue is Full or not."""
        if self.value > 1:
            return True
        else:
            return False

    def procedure_enqueue(self, item):
        """Push new object to queue"""
        if self.rear == len(self.size):
            self.procedure_expand_size()
        self.size[self.rear] = item
        self.rear = self.rear + 1
        self.value = self.value + 1

    def procedure_dequeue(self):
        """Remove first object from queue."""
        if self.is_empty():
            raise DsIndexError()
        item = self.size[self.front]
        self.size[self.front] = None
        self.front = self.front + 1
        self.value = self.value - 1
        return item

    def procedure_expand_size(self):
        """Doubled or expanding object from queue."""
        return len(self.size)

    def procedure_peek(self):
        if self.is_empty():
            raise DsIndexError()
        return self.size[self.front]


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional[str] = None


class CircularQueue:
    def __init__(self):
        # super().__init__()
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        if self.size < 1:
            return True
        else:
            return False

    def procedure_enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.front.next = node
            self.rear = node
        self.size = self.size + 1

    def procedure_dequeue(self):
        if self.is_empty():
            raise DsIndexError()
        value = self.front.value
        if self.front is self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.size = self.size - 1
        return value

    def procedure_peek(self):
        if self.is_empty():
            raise DsPeekIndexError()
        return self.front.value


# Got some error
# Next todo -> fixed bugs in procedure_insert
class PriorityQueue:
    def __init__(self, i: int = 10) -> int:
        """
        Initialize param for heapify.
        :largest: largest among root -> None
        :left: left node
        :right: right node
        """
        self.largest = None
        if self.largest is None:
            self.largest = i
        self.left = 2 * i + 1
        self.right = 2 * i + 2

    def heap(self, n, i, arr):
        """Using Max-heap finding for priority Queue."""

        if self.left < n and arr[i] < arr[self.left]:
            largest = self.left

        if self.right < n and arr[i] < arr[self.right]:
            largest = self.right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            return self.heap(arr, n, largest)

    def procedure_insert(self):
        size = Queue()
        if size == 0:
            Queue.procedure_enqueue()
        else:
            Queue.procedure_enqueue()
            for i in range((size // 2) - 1, -1, -1):
                self.heap(Queue, size, i)

    def procedure_delete(self):
        size = Queue()
        i = 0
        for i in range(0, size):
            if size == Queue[i]:
                break

        Queue[i], Queue[size - 1] = Queue[size - 1], Queue[i]

        Queue.procedure_dequeue(size - 1)

        for i in range((len(Queue) // 2) - 1, -1, -1):
            self.heap(Queue, len(Queue), i)
