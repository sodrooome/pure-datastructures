class Node:

    def __init__(self, data):
        """
        Initialize List node. params:
        :data: data -> Any
        :next: frame or None
        :value: selected value
        """
        super().__init__()
        self.data = data
        self.next = None
        #self.value = value

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

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
            raise ValueError
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
            raise ValueError
        node.value = node.next.value
        node.next = node.next.next