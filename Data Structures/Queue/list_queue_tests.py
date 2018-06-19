import unittest
from list_queue import *

class TestQueue(unittest.TestCase):

    def test_repr(self):
        queue = empty_queue()
        self.assertEqual(repr(queue), "ListQueue(None, None)")

    def test_empty_queue(self):
        self.assertEqual(empty_queue(), ListQueue())

    def test_enqueue_empty(self):
        queue = empty_queue()
        queue = enqueue(queue, 8)
        q = empty_queue()
        q.forward = None
        q.backward = Pair(8, None)
        self.assertEqual(queue, q)

    def test_enqueue(self):
        queue = empty_queue()
        queue = enqueue(queue, 8)
        q = empty_queue()
        q.forward = None
        q.backward = Pair(8, None)
        self.assertEqual(queue, q)
        queue = enqueue(queue, 7)
        q.backward = Pair(7, Pair(8, None))
        self.assertEqual(queue, q)

    def test_dequeue_empty(self):
        self.assertRaises(IndexError, dequeue, empty_queue())

    def test_dequeue(self):
        queue = empty_queue()
        queue = enqueue(queue, 9)
        queue = enqueue(queue, 90)
        queue = enqueue(queue, 900)
        queue = enqueue(queue, 9000)
        val, queue = dequeue(queue)
        q = empty_queue()
        q.forward = Pair(90, Pair(900, Pair(9000, None)))
        q.backward = None
        self.assertEqual((val, queue), (9, q))
        queue = enqueue(queue, 5)
        q.backward = Pair(5, None)
        self.assertEqual(queue, q)
        val, queue = dequeue(queue)
        self.assertEqual(val, 90)
        val, queue = dequeue(queue)
        self.assertEqual(val, 900)
        val, queue = dequeue(queue)
        self.assertEqual(val, 9000)
        q.forward = None
        self.assertEqual(queue, q)
        val, queue = dequeue(queue)
        self.assertEqual(val, 5)
        q.backward = None
        self.assertEqual(queue, q)

    def test_large_dequeue(self):
        queue = empty_queue()
        for i in range(5000):
            queue = enqueue(queue, 62)
        val, queue = dequeue(queue)
        self.assertEqual(val, 62)
        self.assertEqual(size(queue), 4999)

    def test_peek_empty(self):
        self.assertRaises(IndexError, peek, empty_queue())

    def test_peek(self):
        queue = empty_queue()
        queue = enqueue(queue, 9)
        queue = enqueue(queue, 90)
        queue = enqueue(queue, 900)
        queue = enqueue(queue, 9000)
        self.assertEqual(peek(queue), 9)
        val, queue = dequeue(queue)
        self.assertEqual(peek(queue), 90)

    def test_size_empty(self):
        self.assertEqual(size(empty_queue()), 0)

    def test_size(self):
        queue = empty_queue()
        queue = enqueue(queue, 9)
        queue = enqueue(queue, 90)
        queue = enqueue(queue, 900)
        queue = enqueue(queue, 9000)
        self.assertEqual(size(queue), 4)

    def test_is_empty(self):
        queue = empty_queue()
        self.assertEqual(is_empty(queue), True)
        queue = enqueue(queue, 5)
        self.assertEqual(is_empty(queue), False)

    def test_reverse(self):
        backward = Pair(9, Pair(8, Pair(7, None)))
        forward = Pair(7, Pair(8, Pair(9, None)))
        self.assertEqual(reverse(backward), forward)

    def test00_interface(self):
        test_queue = empty_queue()
        test_queue = enqueue(test_queue, "foo")
        peek(test_queue)
        _, test_queue = dequeue(test_queue)
        size(test_queue)
        is_empty(test_queue)

if __name__ == "__main__":
    unittest.main()
