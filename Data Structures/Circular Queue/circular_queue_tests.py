import unittest
from circular_queue import *

class TestQueue(unittest.TestCase):

    def test_repr(self):
        queue = empty_queue()
        st = [None] * 5000
        self.assertEqual(repr(queue), "Queue(" + str(st) + ", 0, 0, 0)")

    def test_empty_queue(self):
        self.assertEqual(empty_queue(), Queue())

    def test_enqueue(self):
        queue = empty_queue()
        queue = enqueue(queue, 8)
        lister = [None] * 5000
        lister[0] = 8
        q = empty_queue()
        q.array = lister
        q.front = 0
        q.back = 0
        q.size = 1
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
        lister = [None] * 5000
        lister[0] = 9
        lister[1] = 90
        lister[2] = 900
        lister[3] = 9000
        q = empty_queue()
        q.array = lister
        q.front = 1
        q.back = 3
        q.size = 3
        self.assertEqual(val, 9)
        self.assertEqual(queue, q)
        queue = enqueue(queue, 5)
        lister[4] = 5
        q.array = lister
        q.back = 4
        q.size = 4
        self.assertEqual(queue, q)
        val, queue = dequeue(queue)
        self.assertEqual(val, 90)
        val, queue = dequeue(queue)
        self.assertEqual(val, 900)
        val, queue = dequeue(queue)
        self.assertEqual(val, 9000)
        q.array = lister
        q.front = 4
        q.back = 4
        q.size = 1
        self.assertEqual(queue, q)
        val, queue = dequeue(queue)
        self.assertEqual(val, 5)
        q.array = lister
        q.front = 4
        q.back = 4
        q.size = 0
        self.assertEqual(queue, q)
        lister = [1] * 5000
        queue.array = lister
        queue.back = 4999
        queue.front = 1
        queue.size = 4999
        queue = enqueue(queue, 5)
        lister[0] = 5
        q.array = lister
        q.back = 0
        q.front = 1
        q.size = 5000
        self.assertEqual(queue, q)
        lister[0] = 5
        lister[4998] = None
        lister[4999] = 55
        queue.array = lister
        queue.back = 4997
        queue.front = 4999
        queue.size = 4999
        val, queue = dequeue(queue)
        q.array = lister
        q.back = 4997
        q.front = 0
        q.size = 4998
        self.assertEqual(val, 55)
        self.assertEqual(queue, q)
        queue = enqueue(queue, 9)
        queue = enqueue(queue, 9)
        self.assertRaises(IndexError, enqueue, queue, 9)

    def test_dequeue_large(self):
        queue = empty_queue()
        for i in range(5000):
            queue = enqueue(queue, i)
        for i in range(5000):
            val, queue = dequeue(queue)
        for i in range(5000):
            queue = enqueue(queue, i)
        for i in range(5000):
            val, queue = dequeue(queue)
        queue = enqueue(queue, 61)
        self.assertEqual(peek(queue), 61)
        queue = enqueue(queue, 98)
        queue = enqueue(queue, 847)
        self.assertEqual(peek(queue), 61)
        val, queue = dequeue(queue)
        self.assertEqual(peek(queue), 98)

    def test_peek_empty(self):
        self.assertRaises(IndexError, peek, empty_queue())

    def test_peek(self):
        queue = empty_queue()
        queue = enqueue(queue, 9)
        queue = enqueue(queue, 90)
        queue = enqueue(queue, 900)
        queue = enqueue(queue, 9000)
        self.assertEqual(peek(queue), 9)

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

    def test00_interface(self):
        test_queue = empty_queue()
        test_queue = enqueue(test_queue, "foo")
        peek(test_queue)
        _, test_queue = dequeue(test_queue)
        size(test_queue)
        is_empty(test_queue)

if __name__ == "__main__":
    unittest.main()
