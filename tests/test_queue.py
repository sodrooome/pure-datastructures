import unittest

from ds.ds_queue import Queue, CircularQueue


class TestQueue(unittest.TestCase):
    def test_queue(self):
        queue = Queue()
        queue.procedure_enqueue(1)
        queue.procedure_enqueue(2)
        queue.procedure_enqueue(3)

        # test for peek the top-most-element
        self.assertEqual(1, queue.procedure_peek())

        # remove top most of value
        self.assertEqual(1, queue.procedure_dequeue())

        # expand size of queue
        self.assertEqual(10, queue.procedure_expand_size())

    def test_circularqueue(self):
        queue = CircularQueue()
        queue.procedure_enqueue(3)
        queue.procedure_enqueue(2)
        queue.procedure_enqueue(1)

        # test for peek the top-most-element
        self.assertEqual(3, queue.procedure_peek())

        # remove top most of value
        self.assertEqual(3, queue.procedure_dequeue())


if __name__ == "__main__":
    unittest.main()
