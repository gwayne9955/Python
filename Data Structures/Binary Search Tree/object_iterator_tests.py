#
# Garrett Wayne
#

import unittest
from linked_list import *

class TestList(unittest.TestCase):

    def test_eq(self):
        it = object_iterator(Pair(1, Pair(4, Pair(7, Pair(2, Pair(1, None))))))
        it_2 = object_iterator(Pair(1, Pair(4, Pair(7, Pair(2, Pair(1, None))))))
        self.assertEqual(it, it_2)

    def test_repr(self):
        it = object_iterator(Pair(1, Pair(4, Pair(7, Pair(2, Pair(1, None))))))
        self.assertEqual(repr(it), "Iterator(Pair(1, Pair(4, Pair(7, Pair(2, Pair(1, None))))))")

    def test_object_iterator(self):
        lister = Pair(1, Pair(4, Pair(7, Pair(2, Pair(1, None)))))
        it = object_iterator(lister)
        self.assertEqual(object_iterator(lister), Iterator(lister))

    def test_empty_iterator(self):
        self.assertEqual(object_iterator(None), Iterator(None))

    def test_has_next_empty(self):
        it = object_iterator(None)
        self.assertEqual(has_next(it), False)
        it.lst = Pair(1, None)
        self.assertEqual(has_next(it), True)
        next(it)
        self.assertEqual(has_next(it), False)

    def test_has_next(self):
        it = object_iterator(Pair(1, Pair(4, Pair(7, Pair(2, Pair(1, None))))))
        self.assertEqual(has_next(it), True)
        next(it)
        self.assertEqual(has_next(it), True)
        next(it)
        self.assertEqual(has_next(it), True)
        next(it)
        self.assertEqual(has_next(it), True)
        next(it)
        self.assertEqual(has_next(it), True)
        next(it)
        self.assertEqual(has_next(it), False)

    def test_next_empty(self):
        it = object_iterator(None)
        self.assertRaises(StopIteration, next, it)

    def test_next(self):
        it = object_iterator(Pair(1, Pair(4, Pair(7, Pair(2, Pair(1, None))))))
        self.assertEqual(next(it), 1)
        self.assertEqual(next(it), 4)
        self.assertEqual(next(it), 7)
        self.assertEqual(next(it), 2)
        self.assertEqual(next(it), 1)
        self.assertRaises(StopIteration, next, it)

if __name__ == '__main__':
    unittest.main()
