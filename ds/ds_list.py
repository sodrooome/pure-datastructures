from typing import Optional, Any
from .exception import DsValueError, DsIndexError


class Node:
    def __init__(self, data: object) -> None:
        """
        Initialize List node. params:
        :data: data -> Any
        :next: frame or None
        :value: selected value
        """
        self.data = data
        self.next: Optional[str] = None
        self.previous: Optional[str] = None
        # self.value = value

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.previous

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class OrderedList:
    def __init__(self):
        self.head: Optional[str] = None

    def procedure_search_obj(self, item):
        """Searching value through list."""
        current = self.head
        found = False
        stop = False

        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found

    def procedure_push(self, item):
        """Push value without hold in temporary object."""
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temporary = Node(item)
        if previous is None:
            temporary.set_next(self.head)
            self.head = temporary
        else:
            temporary.set_next(current)
            previous.set_next(temporary)

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return self.head == self.head + 1

    def procedure_expand_size(self):
        """Expand value of list."""
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    def procedure_delete_node(self):
        """Function to delete node with specific value."""
        node = Node()
        if node is None or node.next is None:
            raise DsValueError()
        node.value = node.next.value
        node.next = node.next.next


class UnorderedList:
    def __init__(self):
        self.head: Optional[str] = None

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return self.head == self.head + 1

    def procedure_push(self, item):
        """Append a new object to list. Using 0(n)."""
        temporary = Node(item)
        temporary.set_next(self.head)
        self.head = temporary

    def procedure_expand_size(self):
        count = 0
        current = self.head
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    def procedure_search_obj(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def procedure_delete_node(self):
        node = Node()
        if node is not None or node.next is None:
            raise DsValueError()
        node.value = node.next.value
        node.next = node.next.next


# It's working but not returning a value
# instead, it will return None
class DoubleLinkedList:
    def __init__(self):
        self.previous = None
        self.head: Optional[str] = None

    def procedure_insert(self, data: object) -> Any:
        """Inserting items if list is empty."""
        if self.head is None:
            node = Node(data)
            self.head = node
        else:
            raise DsIndexError()

    def procedure_insert_start(self, data):
        """Inserting items in beginning of list."""
        if self.head is None:
            node = Node(data)
            self.head = node
            return
        node = Node(data)
        node.next = self.head
        self.head.previous = node
        self.head = node

    def procedure_insert_end(self, data, node=None):
        """Inserting items in last of list."""
        if self.head is None:
            node = Node(data)
            self.head = node
            return
        n = node
        while n.get_next() is not None:
            n = n.get_next()
        node = Node(data)
        n.next = node
        node.previous = n

    def procedure_delete_node(self):
        """Delete items at the beginning of list."""
        if self.head is None:
            raise DsIndexError()
        if self.head.get_next() is None:
            self.head = None
            return
        self.head = self.head.next

    def procedure_search_obj(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found
