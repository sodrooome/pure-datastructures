class Queue:

    def __init__(self, maxsize=10):
        """
        Initialize Queue. params:
        :size: Array and empty
        :front: integers and null
        :rear: integers and null
        :value: integers and null
        """
        super().__init__()
        self.front = 0
        self.rear = 0
        self.value = 0
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
            raise IndexError("Queue is empty.")
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
            raise IndexError("Queue is empty.")
        return self.size[self.front]

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class CircularQueue:

    def __init__(self):
        super().__init__()
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
            raise IndexError("Queue is empty, set a value first.")
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
            raise IndexError("Queue is empty, you either must be popped or not set a value.")
        return self.front.value

class BalancedParenthesis:

    def is_balanced(parenthesis):
        """Use Queue class to checking valid parenthesis."""
        queue = Queue(len(parenthesis))
        for ps in parenthesis:
            if ps == "(":
                queue.procedure_enqueue(ps)
            elif ps == ")":
                if queue.is_empty():
                    return "Queue is unbalanced."
                queue.procedure_dequeue()
        return queue.is_empty()
