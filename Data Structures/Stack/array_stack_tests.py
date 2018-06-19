import unittest
from array_stack import *

class TestStack(unittest.TestCase):

    def test_repr(self):
        stack = empty_stack()
        push(stack, 1)
        push(stack, 2)
        push(stack, 3)
        self.assertEqual(repr(stack), "Stack([1, 2, 3, None, None], 3, 5)")

    def test_eq_not_equal(self):
        stack = Stack()
        push(stack, 3)
        stack_2 = Stack()
        self.assertEqual(stack == stack_2, False)
        push(stack_2, 33)
        self.assertEqual(stack == stack_2, False)

    def test_empty_stack(self):
        self.assertEqual(empty_stack(), Stack())

    def test_push_empty(self):
        stack_1 = empty_stack()
        push(stack_1, 4)
        self.assertEqual(push(empty_stack(), 4), stack_1)

    def test_push(self):
        stack_1 = empty_stack()
        push(stack_1, 8)
        push(stack_1, 7)
        push(stack_1, 2)
        push(stack_1, 5)
        push(stack_1, 4)
        push(stack_1, 99)
        self.assertEqual(push(push(push(push(push(push(empty_stack(), 8), 7), 2), 5), 4), 99), stack_1)

    def test_pop_empty(self):
        self.assertRaises(IndexError, pop, empty_stack())

    def test_pop(self):
        stack = empty_stack()
        push(stack, 9)
        push(stack, 90)
        push(stack, 900)
        push(stack, 9000)
        val, stack = pop(stack)
        self.assertEqual((val, stack), (9000, push(push(push(empty_stack(), 9), 90), 900)))
        push(stack, 5)
        self.assertEqual(stack, push(push(push(push(empty_stack(), 9), 90), 900), 5))
        val, stack = pop(stack)
        val, stack = pop(stack)
        val, stack = pop(stack)
        self.assertEqual(stack, push(empty_stack(), 9))

    def test_peek_empty(self):
        self.assertRaises(IndexError, peek, empty_stack())

    def test_peek(self):
        stack = empty_stack()
        push(stack, 9)
        push(stack, 90)
        push(stack, 900)
        push(stack, 9000)
        self.assertEqual(peek(stack), 9000)

    def test_size_empty(self):
        self.assertEqual(size(empty_stack()), 0)

    def test_size(self):
        stack = empty_stack()
        push(stack, 9)
        push(stack, 90)
        push(stack, 900)
        push(stack, 9000)
        self.assertEqual(size(stack), 4)

    def test_is_empty(self):
        stack = empty_stack()
        self.assertEqual(is_empty(stack), True)
        push(stack, 5)
        self.assertEqual(is_empty(stack), False)

    def test_grow_empty(self):
        stack = Stack()
        stack_2 = Stack()
        stack_2.array = [None] * stack.capacity * 2
        stack_2.capacity = stack.capacity * 2
        grow(stack)
        self.assertEqual(stack, stack_2)

    def test_grow_1(self):
        stack = Stack()
        stack.array = [1, 21, 3, 5, None]
        stack.size = 4
        stack_2 = Stack()
        stack_2.array = [1, 21, 3, 5, None, None, None, None, None]
        stack_2.size = 4
        stack_2.capacity = stack.capacity * 2
        grow(stack)
        self.assertEqual(stack, stack_2)

    def test00_interface(self):
        test_stack = empty_stack()
        test_stack = push(test_stack, "foo")
        peek(test_stack)
        _, test_stack = pop(test_stack)
        size(test_stack)
        is_empty(test_stack)

if __name__ == "__main__":
    unittest.main()
