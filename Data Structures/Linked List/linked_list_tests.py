#
# Garrett Wayne
#

import unittest
from linked_list import *

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.

    def test_repr(self):
        self.assertEqual(repr(Pair(3, Pair(4, None))), "Pair(3, Pair(4, None))")
        self.assertEqual(repr(Pair(1, Pair(2, Pair(3, None)))), "Pair(1, Pair(2, Pair(3, None)))")

    def test_empty_list(self):
        self.assertEqual(empty_list(), None)

    def test_add_empty(self):
        self.assertEqual(add(None, 0, 4), Pair(4, None))

    def test_add(self):
        self.assertRaises(IndexError, add, Pair(3, Pair(6, None)), -1, 4)
        self.assertRaises(IndexError, add, Pair(3, Pair(6, None)), 4, 4)
        self.assertRaises(IndexError, add, Pair(4, Pair(3, Pair(6, None))), 4, 4)
        self.assertEqual(add(Pair(1, Pair(4, Pair(7, Pair(2, Pair(1, None))))), 3, 4),
        Pair(1, Pair(4, Pair(7, Pair(4, Pair(2, Pair(1, None)))))))
        self.assertRaises(IndexError, add,
        Pair(1, Pair(4, Pair(7, Pair(2, Pair(1, None))))), -1, 4)
        self.assertEqual(add(Pair(3, Pair(4, None)), 0, 2), Pair(2, Pair(3, Pair(4, None))))
        self.assertEqual(add(Pair(2, Pair(3, Pair(4, None))), 1, 5),
        Pair(2, Pair(5, Pair(3, Pair(4, None)))))
        self.assertEqual(add(Pair(2, Pair(3, Pair(4, None))), 2, 5),
        Pair(2, Pair(3, Pair(5, Pair(4, None)))))
        self.assertEqual(add(Pair(2, Pair(3, Pair(4, None))), 3, 5),
        Pair(2, Pair(3, Pair(4, Pair(5, None)))))

    def test_length_empty(self):
        self.assertEqual(length(None), 0)

    def test_length(self):
        self.assertEqual(length(Pair(1, None)), 1)
        self.assertEqual(length(Pair(1, Pair(2, None))), 2)
        self.assertEqual(length(Pair(None, Pair(None, Pair(None, None)))), 3)
        self.assertEqual(length(Pair(1, Pair(2, Pair(3, None)))), 3)

    def test_get_empty(self):
        self.assertRaises(IndexError, get, None, 0)

    def test_get(self):
        self.assertRaises(IndexError, get, Pair(3, Pair(5, None)), -1)
        self.assertRaises(IndexError, get, Pair(4, Pair(3, Pair(5, None))), 3)
        self.assertRaises(IndexError, get, Pair(4, Pair(3, Pair(5, None))), 4)
        self.assertEqual(get(Pair(4, Pair(3, Pair(5, None))), 0), 4)
        self.assertEqual(get(Pair("jim", Pair("tom", Pair("joe", None))), 1), "tom")
        self.assertEqual(get(Pair(4, Pair(3, Pair(5, None))), 2), 5)

    def test_set_empty(self):
        self.assertRaises(IndexError, set, None, 0, 1)

    def test_set(self):
        self.assertRaises(IndexError, set, Pair(3, Pair(5, None)), -2, 0)
        self.assertRaises(IndexError, set, Pair(3, Pair(5, None)), 2, 7)
        self.assertEqual(set(Pair(1, Pair(4, Pair(7, Pair(2, Pair(1, None))))), 3, 77),
        Pair(1, Pair(4, Pair(7, Pair(77, Pair(1, None))))))
        self.assertEqual(set(Pair(3, Pair(4, Pair(5, None))), 0, 0),
        Pair(0, Pair(4, Pair(5, None))))
        self.assertEqual(set(Pair(3, Pair(4, Pair(5, None))), 1, 0),
        Pair(3, Pair(0, Pair(5, None))))
        self.assertEqual(set(Pair(3, Pair(4, Pair(5, None))), 2, 0),
        Pair(3, Pair(4, Pair(0, None))))

    def test_remove_empty(self):
        self.assertRaises(IndexError, remove, None, 0)

    def test_remove(self):
        self.assertRaises(IndexError, remove, Pair(3, Pair(5, None)), -1)
        self.assertRaises(IndexError, remove, Pair(4, Pair(3, Pair(5, None))), 3)
        self.assertRaises(IndexError, remove, Pair(4, Pair(3, Pair(5, None))), 4)
        self.assertEqual(remove(Pair(1, Pair(2, Pair(3, None))), 1), (2, Pair(1, Pair(3, None))))
        self.assertEqual(remove(Pair(2, Pair(3, Pair(4, None))), 0), (2, Pair(3, Pair(4,None))))
        self.assertEqual(remove(Pair(2, Pair(3, Pair(4, None))), 1), (3, Pair(2, Pair(4, None))))
        self.assertEqual(remove(Pair(2, Pair(3, Pair(4, Pair(5, Pair(6, None))))), 3),
        (5, Pair(2, Pair(3, Pair(4, Pair(6, None))))))
        self.assertEqual(remove(Pair(2, Pair(3, Pair(4, None))), 2), (4, Pair(2, Pair(3,None))))

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

        test_list = Pair(1, Pair(2, Pair(3, None)))
        expected_list = [2, 3, 4]
        foreach(test_list, the_func)
        self.assertEqual(gather, expected_list)

    def test_sort(self):
        def less_than(val_1, val_2):
            if val_1 < val_2:
                return True
            elif val_1 > val_2:
                return False
            else:
                return True
        self.assertEqual(sort(Pair(3, Pair(5, Pair(8, Pair(2, Pair(4, None))))), less_than),
        Pair(2, Pair(3, Pair(4, Pair(5, Pair(8, None))))))
        self.assertEqual(sort(Pair(5, Pair(5, Pair(8, Pair(2, Pair(4, None))))), less_than),
        Pair(2, Pair(4, Pair(5, Pair(5, Pair(8, None))))))

if __name__ == '__main__':
    unittest.main()
