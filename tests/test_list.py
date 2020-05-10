import unittest

from ds.ds_list import OrderedList, UnorderedList

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

if __name__ == "__main__":
    unittest.main()
