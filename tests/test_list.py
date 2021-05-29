import unittest

from ds.ds_list import OrderedList, UnorderedList, DoubleLinkedList


class ListTestCase(unittest.TestCase):
    def test_ordered_list(self):
        olist = OrderedList()
        olist.procedure_push(1)
        olist.procedure_push(2)
        olist.procedure_push(3)

        # test for searching a object
        self.assertEqual(True, olist.procedure_search_obj(3))

        # doubled size an array
        self.assertEqual(3, olist.procedure_expand_size())

    def test_unordered_list(self):
        olist = UnorderedList()
        olist.procedure_push(1)
        olist.procedure_push(2)
        olist.procedure_push(3)

        # test for searching a object
        self.assertEqual(True, olist.procedure_search_obj(2))

        # expand size an array
        self.assertEqual(3, olist.procedure_expand_size())

    def test_double_linkedlist(self):
        olist = DoubleLinkedList()
        olist.procedure_insert(1)
        olist.procedure_insert(3)
        olist.procedure_insert(5)

        # test if inserting items in beginning is work
        self.assertTrue(True, olist.procedure_insert_start(51))

        # test for searching an object
        self.assertEqual(True, olist.procedure_search_obj(1))


if __name__ == "__main__":
    unittest.main()
