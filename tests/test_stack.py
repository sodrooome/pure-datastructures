import unittest

from ds.ds_stack import Stack, LinkedList

class TestStack(unittest.TestCase):
	def test_stacK(self):
		stack = Stack()
		stack.procedure_push(1)
		stack.procedure_push(2)
		stack.procedure_push(3)

		# test for peek the top-most value
		self.assertEqual(3, stack.procedure_peek())

		# test for remove value from stack
		self.assertEqual(3, stack.procedure_pop())

	def test_linkedlist(self):
		stack = LinkedList()
		stack.procedure_push(3)
		stack.procedure_push(2)
		stack.procedure_push(1)

		# test stack if is empty
		self.assertFalse(stack.is_empty())

		# test for peek the top-most value
		self.assertEqual(1, stack.procedure_peek())

		# test for remove value from stack
		self.assertEqual(1, stack.procedure_pop())

if __name__ == "__main__":
    unittest.main()