#
# Garrett Wayne
#

import unittest
from linked_stack import *

class TestStack(unittest.TestCase):

    def test_repr(self):
        self.assertEqual(repr(Pair(3, Pair(4, None))), "Pair(3, Pair(4, None))")
        self.assertEqual(repr(Pair(1, Pair(2, Pair(3, None)))), "Pair(1, Pair(2, Pair(3, None)))")

    def test_empty_stack(self):
        self.assertEqual(empty_stack(), None)

    def test_push_empty(self):
        self.assertEqual(push(None, 4), Pair(4, None))

    def test_push(self):
        stack = empty_stack()
        stack = push(stack, 8)
        self.assertEqual(stack, Pair(8, None))
        stack = push(stack, 7)
        self.assertEqual(stack, Pair(7, Pair(8, None)))

    def test_pop_empty(self):
        self.assertRaises(IndexError, pop, empty_stack())

    def test_pop(self):
        stack = empty_stack()
        stack = push(stack, 9)
        stack = push(stack, 90)
        stack = push(stack, 900)
        stack = push(stack, 9000)
        val, stack = pop(stack)
        self.assertEqual((val, stack), (9000, Pair(900, Pair(90, Pair(9, None)))))
        stack = push(stack, 5)
        self.assertEqual(stack, Pair(5, Pair(900, Pair(90, Pair(9, None)))))
        val, stack = pop(stack)
        val, stack = pop(stack)
        val, stack = pop(stack)
        self.assertEqual(stack, Pair(9, None))

    def test_peek_empty(self):
        self.assertRaises(IndexError, peek, empty_stack())

    def test_peek(self):
        stack = empty_stack()
        stack = push(stack, 9)
        stack = push(stack, 90)
        stack = push(stack, 900)
        stack = push(stack, 9000)
        self.assertEqual(peek(stack), 9000)

    def test_size_empty(self):
        self.assertEqual(size(empty_stack()), 0)

    def test_size(self):
        stack = empty_stack()
        stack = push(stack, 9)
        stack = push(stack, 90)
        stack = push(stack, 900)
        stack = push(stack, 9000)
        self.assertEqual(size(stack), 4)

    def test_is_empty(self):
        stack = empty_stack()
        self.assertEqual(is_empty(stack), True)
        stack = push(stack, 5)
        self.assertEqual(is_empty(stack), False)

    def test00_interface(self):
        test_stack = empty_stack()
        test_stack = push(test_stack, "foo")
        peek(test_stack)
        _, test_stack = pop(test_stack)
        size(test_stack)
        is_empty(test_stack)

if __name__ == "__main__":
    unittest.main()
