import unittest
from linked_list import yield_iterator, Pair

class TestList(unittest.TestCase):

    def test_yield_iterator_empty(self):
        lister = None
        yielder = yield_iterator(lister)
        self.assertRaises(StopIteration, next, yielder)

    def test_yield_iterator(self):
        lister = Pair(1, Pair(4, Pair(7, Pair(2, Pair(1, None)))))
        yielder = yield_iterator(lister)
        self.assertEqual(next(yielder), 1)
        self.assertEqual(next(yielder), 4)
        self.assertEqual(next(yielder), 7)
        self.assertEqual(next(yielder), 2)
        self.assertEqual(next(yielder), 1)
        self.assertRaises(StopIteration, next, yielder)

if __name__ == '__main__':
    unittest.main()
