import unittest
from bst import *

class TestList(unittest.TestCase):

    def test_prefix_iterator_empty(self):
        tree = BinarySearchTree(comes_before)
        yielder = prefix_iterator(tree)
        self.assertRaises(StopIteration, next, yielder)

    def test_prefix_iterator(self):
        tree = BinarySearchTree(comes_before)
        tree.root = BSTNode(22, BSTNode(13, None, BSTNode(16, None, None)), None)
        yielder = prefix_iterator(tree)
        self.assertEqual(next(yielder), 22)
        self.assertEqual(next(yielder), 13)
        self.assertEqual(next(yielder), 16)
        self.assertRaises(StopIteration, next, yielder)

    def test_infix_iterator_empty(self):
        tree = BinarySearchTree(comes_before)
        yielder = infix_iterator(tree)
        self.assertRaises(StopIteration, next, yielder)

    def test_infix_iterator(self):
        tree = BinarySearchTree(comes_before)
        tree.root = BSTNode(22, BSTNode(13, None, BSTNode(16, None, None)), None)
        yielder = infix_iterator(tree)
        self.assertEqual(next(yielder), 13)
        self.assertEqual(next(yielder), 16)
        self.assertEqual(next(yielder), 22)
        self.assertRaises(StopIteration, next, yielder)

    def test_postfix_iterator_empty(self):
        tree = BinarySearchTree(comes_before)
        yielder = postfix_iterator(tree)
        self.assertRaises(StopIteration, next, yielder)

    def test_postfix_iterator(self):
        tree = BinarySearchTree(comes_before)
        tree.root = BSTNode(22, BSTNode(13, None, BSTNode(16, None, None)), None)
        yielder = postfix_iterator(tree)
        self.assertEqual(next(yielder), 16)
        self.assertEqual(next(yielder), 13)
        self.assertEqual(next(yielder), 22)
        self.assertRaises(StopIteration, next, yielder)

if __name__ == '__main__':
    unittest.main()
