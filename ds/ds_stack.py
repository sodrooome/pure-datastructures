class Stack:

	def __init__(self, maxsize=10):
		"""
		Initialize stack. params:
		:items: array and empty
		:maxsize: size of array
		:top: integer
		"""
		super().__init__()
		self.items = []
		self.top = 0
		self.array = [None] * maxsize

	def __iter__(self):
		probe = self.top
		while True:
			if probe == -1:
				return
			yield self.array[probe]
			probe = probe - 1

	def __str__(self):
		result = " ".join(map(str, self))
		return 'Top - ' + result

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
			raise IndexError("Stack is empty.")
		item = self.array[self.top]
		self.top = self.top - 1
		return item

	def procedure_peek(self):
		"""Check the top-most element of the stack."""
		if self.is_empty():
			raise IndexError("Stack is empty.")
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
		self.next = None

	def __repr__(self):
		return self.data

class LinkedList:

	def __init__(self):
		super().__init__()
		self.head = None
		self.top = 0

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
			raise IndexError("Stack is empty, set a value first.")
		data = self.head.data
		self.head = self.head.next
		self.top = self.top - 1
		return data

	def procedure_peek(self):
		if self.is_empty():
			raise IndexError("Stack is empty, you either must be popped or not set a value.")
		return self.head.data

class BalancedParenthesis:

    def is_balanced(parenthesis):
        """Use Stack class to checking valid parenthesis."""
        stack = Stack(len(parenthesis))
        for ps in parenthesis:
            if ps == "(":
                stack.procedure_push(ps)
            elif ps == ")":
                if stack.is_empty():
                    return "Stack is unbalanced."
                stack.procedure_pop()
        return stack.is_empty()
