import unittest
from priority_queue import *

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.

    def test_repr(self):
        self.assertEqual(repr(Pair(3, Pair(4, None))), "Pair(3, Pair(4, None))")
        self.assertEqual(repr(Pair(1, Pair(2, Pair(3, None)))), "Pair(1, Pair(2, Pair(3, None)))")

    def test_repr_2(self):
        self.assertEqual(repr(empty_pqueue(comes_before)), "PriorityQueue('comes_before', None)")

    def test_empty_pqueue(self):
        pq = empty_pqueue(comes_before)
        self.assertEqual(empty_pqueue(comes_before), pq)

    def test_enqueue_empty(self):
        self.assertEqual(enqueue(empty_pqueue(comes_before), 4).list, Pair(4, None))

    def test_enqueue(self):
        pqueue = empty_pqueue(comes_before)
        pqueue = enqueue(pqueue, 8)
        self.assertEqual(pqueue.list, Pair(8, None))
        pqueue = enqueue(pqueue, 7)
        self.assertEqual(pqueue.list, Pair(7, Pair(8, None)))

    def test_dequeue_empty(self):
        self.assertRaises(IndexError, dequeue, empty_pqueue(comes_before))

    def test_dequeue(self):
        pqueue = empty_pqueue(comes_before)
        pqueue = enqueue(pqueue, 9)
        pqueue = enqueue(pqueue, 90)
        pqueue = enqueue(pqueue, 900)
        pqueue = enqueue(pqueue, 9000)
        val, pqueue = dequeue(pqueue)
        self.assertEqual((val, pqueue.list), (9, Pair(90, Pair(900, Pair(9000, None)))))
        pqueue = enqueue(pqueue, 5)
        self.assertEqual(pqueue.list, Pair(5, Pair(90, Pair(900, Pair(9000, None)))))
        val, pqueue = dequeue(pqueue)
        val, pqueue = dequeue(pqueue)
        val, pqueue = dequeue(pqueue)
        self.assertEqual(pqueue.list, Pair(9000, None))

    def test_peek_empty(self):
        self.assertRaises(IndexError, peek, empty_pqueue(comes_before))

    def test_peek(self):
        pqueue = empty_pqueue(comes_before)
        pqueue = enqueue(pqueue, 9)
        pqueue = enqueue(pqueue, 90)
        pqueue = enqueue(pqueue, 900)
        pqueue = enqueue(pqueue, 9000)
        self.assertEqual(peek(pqueue), 9)

    def test_size_empty(self):
        self.assertEqual(size(empty_pqueue(comes_before)), 0)

    def test_size(self):
        pqueue = empty_pqueue(comes_before)
        pqueue = enqueue(pqueue, 9)
        pqueue = enqueue(pqueue, 90)
        pqueue = enqueue(pqueue, 900)
        pqueue = enqueue(pqueue, 9000)
        self.assertEqual(size(pqueue), 4)

    def test_is_empty(self):
        pqueue = empty_pqueue(comes_before)
        self.assertEqual(is_empty(pqueue), True)
        pqueue = enqueue(pqueue, 5)
        self.assertEqual(is_empty(pqueue), False)

if __name__ == '__main__':
    unittest.main()
