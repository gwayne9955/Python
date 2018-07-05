#
# Garrett Wayne
#

import  unittest
from redBlackTree import *

class TestCases(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(repr(Node("B", 6.5, None, None)),
        "Node('B', 6.5, None, None)")

    def test_eq(self):
        self.assertEqual(Node("B", 6.5, None, None), Node("B", 6.5, None, None))
        self.assertEqual(Node("B", 13, Node("R", 4, None, None), None), Node("B", 13, Node("R", 4, None, None), None))

    def test_is_empty(self):
        self.assertEqual(is_empty(Node("B", 15, None, None)), False)
        self.assertEqual(is_empty(None), True)

    def test_insert(self):
        RBTree = insert(None, 51)
        self.assertEqual(RBTree, Node("B", 51, None, None))
        RBTree = insert(RBTree, 21)
        self.assertEqual(RBTree, Node("B", 51, Node("R", 21, None, None), None))
        RBTree = insert(RBTree, 124)
        self.assertEqual(RBTree, Node("B", 51, Node("R", 21, None, None), Node("R", 124, None, None)))
        RBTree = insert(RBTree, 33)
        self.assertEqual(RBTree, Node("B", 33, Node("B", 21, None, None), Node("B", 51, None, Node("R", 124, None, None))))
        RBTree = insert(RBTree, 92)
        self.assertEqual(RBTree, Node('B', 33, Node('B', 21, None, None), Node('R', 92, Node('B', 51, None, None), Node('B', 124, None, None))))
        RBTree = insert(RBTree, 27)
        self.assertEqual(RBTree, Node('B', 33, Node('B', 21, None, Node("R", 27, None, None)), Node('R', 92, Node('B', 51, None, None), Node('B', 124, None, None))))

    def test_lookup(self):
        RBTree = insert(None, 5)
        self.assertEqual(lookup(RBTree, 6), False)
        self.assertEqual(lookup(RBTree, 5), True)
        RBTree = insert(RBTree, 1)
        self.assertEqual(lookup(RBTree, 1), True)
        self.assertEqual(lookup(RBTree,12), False)
        RBTree = insert(RBTree, 11)
        self.assertEqual(lookup(RBTree, 1), True)
        self.assertEqual(lookup(RBTree, 11), True)
        self.assertEqual(lookup(RBTree, 5), True)
        self.assertEqual(lookup(RBTree,12), False)

    def test_delete(self):
        RBTree = insert(None, 51)
        self.assertEqual(RBTree, Node("B", 51, None, None))
        RBTree = insert(RBTree, 21)
        self.assertEqual(RBTree, Node("B", 51, Node("R", 21, None, None), None))
        RBTree = insert(RBTree, 124)
        self.assertEqual(RBTree, Node("B", 51, Node("R", 21, None, None), Node("R", 124, None, None)))
        RBTree = delete(RBTree, 21)
        self.assertEqual(RBTree, Node("B", 51, None, Node("R", 124, None, None)))
        RBTree = delete(RBTree, 51)
        self.assertEqual(RBTree, Node("B", 124, None, None))
        RBTree = delete(RBTree, 124)
        self.assertEqual(RBTree, None)

        RBTree = insert(None, 51)
        self.assertEqual(RBTree, Node("B", 51, None, None))
        RBTree = insert(RBTree, 21)
        self.assertEqual(RBTree, Node("B", 51, Node("R", 21, None, None), None))
        RBTree = insert(RBTree, 124)
        self.assertEqual(RBTree, Node("B", 51, Node("R", 21, None, None), Node("R", 124, None, None)))
        RBTree = insert(RBTree, 33)
        self.assertEqual(RBTree, Node("B", 33, Node("B", 21, None, None), Node("B", 51, None, Node("R", 124, None, None))))
        RBTree = insert(RBTree, 92)
        self.assertEqual(RBTree, Node('B', 33, Node('B', 21, None, None), Node('R', 92, Node('B', 51, None, None), Node('B', 124, None, None))))
        RBTree = insert(RBTree, 27)
        self.assertEqual(RBTree, Node('B', 33, Node('B', 21, None, Node("R", 27, None, None)), Node('R', 92, Node('B', 51, None, None), Node('B', 124, None, None))))

        RBTree = delete(RBTree, 92)

    # def test_find_min(self):
    #     self.assertEqual(find_min(None, None), (None, None))
    #     self.assertEqual(find_min(BSTNode(7, None, None), BSTNode(2, BSTNode(1, None, None),
    #     BSTNode(7, None, None))), (BSTNode(2, BSTNode(1, None, None), BSTNode(7, None, None)),
    #     BSTNode(7, None, None)))

if __name__ == '__main__':
    unittest.main()
