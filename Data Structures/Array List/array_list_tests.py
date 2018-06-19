import unittest
from array_list import *

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.

    def test_empty_list(self):
        self.assertEqual(empty_list(), List())

    def test_add_empty(self):
        lst = List()
        lst_2 = List()
        add(lst_2, 0, 1)
        self.assertEqual(add(lst, 0, 1), lst_2)

    def test_add_1(self):
        lst = List()
        lst_2 = List()
        lst.array = [1, 2, 3, 4, None]
        lst.length = 4
        lst_2.array = [1, 2, 3, 4, 5]
        lst_2.length = 5
        self.assertEqual(add(lst, 4, 5), lst_2)
        self.assertEqual(lst, lst_2)

        lst_2.array = [1, 2, 3, 66, 4, 5, None, None, None, None]
        lst_2.length = 6
        lst_2.capacity = lst.capacity
        self.assertEqual(add(lst, 3, 66), lst_2)
        self.assertEqual(lst, lst_2)

        self.assertRaises(IndexError, add, List(), -1, 3)
        self.assertRaises(IndexError, add, List(), 7, 3)

    def test_length_empty(self):
        self.assertEqual(length(List()), 0)

    def test_length_short(self):
        lst = List()
        lst.array = [1, 21, 3, None, None]
        lst.length = 3
        self.assertEqual(length(lst), 3)
        add(lst, 3, 8)
        self.assertEqual(length(lst), 4)

    def test_length_medium(self):
        lst = List()
        lst.array = [1, 21, 3, 5, None]
        lst.length = 4
        self.assertEqual(length(lst), 4)
        add(lst, 4, 8)
        self.assertEqual(length(lst), 5)

    def test_get_empty(self):
        self.assertRaises(IndexError, get, List(), 0)
        self.assertRaises(IndexError, get, List(), 7)
        self.assertRaises(IndexError, get, List(), -1)

    def test_get_1(self):
        lst = List()
        lst.array = [1, 21, 3, 5, None]
        lst.length = 4
        self.assertEqual(get(lst, 1), 21)
        self.assertRaises(IndexError, get, lst, 4)
        self.assertRaises(IndexError, get, lst, 7)
        self.assertRaises(IndexError, get, lst, -1)

    def test_set_empty(self):
        self.assertRaises(IndexError, set, List(), 0, 1)

    def test_set_1(self):
        lst = List()
        lst.array = [1, 21, 3, 5, None]
        lst.length = 4
        lst_2 = List()
        lst_2.array = [1, -1, 3, 5, None]
        lst_2.length = 4
        self.assertEqual(set(lst, 1, -1), lst_2)
        self.assertRaises(IndexError, set, lst, 4, 12)
        self.assertRaises(IndexError, set, lst, 5, 12)
        self.assertRaises(IndexError, set, lst, -1, 12)

    def test_remove_empty(self):
        self.assertRaises(IndexError, remove, List(), 0)
        self.assertRaises(IndexError, remove, List(), -1)
        self.assertRaises(IndexError, remove, List(), 123)

    def test_remove_1(self):
        lst = List()
        lst.array = [1, 21, 3, 5, None]
        lst.length = 4
        lst_2 = List()
        lst_2.array = [1, 3, 5, None, None]
        lst_2.length = 3
        self.assertEqual(remove(lst, 1), (21, lst_2))
        lst_2.array = [3, 5, None, None, None]
        lst_2.length = 2
        self.assertEqual(remove(lst, 0), (1, lst_2))
        self.assertRaises(IndexError, remove, lst, 2)
        self.assertRaises(IndexError, remove, lst, 123)
        self.assertRaises(IndexError, remove, lst, -1)

    def test_grow_empty(self):
        lst = List()
        lst_2 = List()
        lst_2.array = [None] * lst.capacity * 2
        lst_2.capacity = lst.capacity * 2
        grow(lst)
        self.assertEqual(lst, lst_2)

    def test_grow_1(self):
        lst = List()
        lst.array = [1, 21, 3, 5, None]
        lst.length = 4
        lst_2 = List()
        lst_2.array = [1, 21, 3, 5, None, None, None, None, None]
        lst_2.length = 4
        lst_2.capacity = lst.capacity * 2
        grow(lst)
        self.assertEqual(lst, lst_2)

    def test_repr(self):
        lst = List()
        lst.array = [1, 21, 3, 5, None]
        lst.length = 4
        self.assertEqual(repr(lst), "List([1, 21, 3, 5, None], 4, 5)")

    def test_eq_not_equal(self):
        lst = List()
        add(lst, 0, 3)
        lst_2 = List()
        self.assertEqual(lst == lst_2, False)
        add(lst_2, 0, 33)
        self.assertEqual(lst == lst_2, False)

    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

    def test_foreach(self):
        gather = []

        def the_func(value):
            gather.append(value + 1)

            # build linked list or array list
            # define expected list

        test_list = List()
        test_list.array = [1, 21, 3, 5, None]
        test_list.length = 4
        expected_list = [2, 22, 4, 6]
        foreach(test_list, the_func)
        self.assertEqual(gather, expected_list)

    def test_sort(self):
        def less_than(val_1, val_2):
            if val_1 < val_2:
                return True
            if val_1 > val_2:
                return False
            else:
                return True
        lst = List()
        lst.array = [1, 21, 3, 5, None]
        lst.length = 4
        lst_2 = List()
        lst_2.array = [1, 3, 5, 21, None]
        lst_2.length = 4
        self.assertEqual(sort(lst, less_than), lst_2)
        lst.array = [1, 21, 21, 3, 5,]
        lst.length = 5
        lst_2.array = [1, 3, 5, 21, 21]
        lst_2.length = 5
        self.assertEqual(sort(lst, less_than), lst_2)
        lst.array = [6, 4, 5, 3, 2]
        lst_2.array = [2, 3, 4, 5, 6]
        self.assertEqual(sort(lst, less_than), lst_2)
        lst.array = [55, -123, 2, 1, 7]
        lst_2.array = [-123, 1, 2, 7, 55]
        self.assertEqual(sort(lst, less_than), lst_2)
        lst.array = [3, 5, 2, 8, 4]
        lst_2.array = [2, 3, 4, 5, 8]
        self.assertEqual(sort(lst, less_than), lst_2)

if __name__ == '__main__':
    unittest.main()
