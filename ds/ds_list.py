from exception import DsValueError, DsIndexError

class Node:

    def __init__(self, data):
        """
        Initialize List node. params:
        :data: data -> Any
        :next: frame or None
        :value: selected value
        """
        self.data = data
        self.next = None
        self.previous = None
        #self.value = value

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.previous

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = new_next

class OrderedList:

    def __init__(self):
        self.head = None

    def procedure_search_obj(self, item):
        """Searching value through list."""
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def procedure_push(self, item):
        """Push value without hold in temporary object."""
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temporary = Node(item)
        if previous == None:
            temporary.setNext(self.head)
            self.head = temporary
        else:
            temporary.setNext(current)
            previous.setNext(temporary)

    def is_empty(self):
        return self.head == None

    def is_full(self):
        return self.head == self.head + 1

    def procedure_expand_size(self):
        """Expand value of list."""
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
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
        self.head = None

    def is_empty(self):
        return self.head == None

    def is_full(self):
        return self.head == self.head + 1

    def procedure_push(self, item):
        """Append a new object to list. Using 0(n)."""
        temporary = Node(item)
        temporary.setNext(self.head)
        self.head = temporary

    def procedure_expand_size(self):
        count = 0
        current = self.head
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def procedure_search_obj(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
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
        self.head = None

    def procedure_insert(self, data):
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

    def procedure_insert_end(self, data):
        """Inserting items in last of list."""
        if self.head is None:
            node = Node(data)
            self.head = node
            return
        n = self.node
        while n.getNext() is not None:
            n = n.getNext()
        node = Node(data)
        n.next = node
        node.previous = n

    def procedure_delete_node(self):
        """Delete items at the beginning of list."""
        if self.head is None:
            raise DsIndexError()
            return
        if self.head.getNext() is None:
            self.head = None
            return
        self.head = self.head.next
        self.previous = None

    def procedure_search_obj(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found



    