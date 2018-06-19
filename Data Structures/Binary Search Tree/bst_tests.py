import  unittest
from bst import *

class TestCases(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(repr(BinarySearchTree(comes_before)),
        "BinarySearchTree('comes_before', None)")
        self.assertEqual(repr(BSTNode(10, BSTNode(5, None, None), None)),
        "BSTNode(10, BSTNode(5, None, None), None)")

    def test_eq(self):
        self.assertEqual(BSTNode(5, None, None), BSTNode(5, None, None))
        self.assertEqual(BinarySearchTree(comes_before), BinarySearchTree(comes_before))

    def test_comes_before(self):
        self.assertEqual(comes_before(1,2), True)
        self.assertEqual(comes_before(3,2), False)
        self.assertEqual(comes_before(1,1), False)

    def test_is_empty(self):
        BTree = BinarySearchTree(comes_before)
        BTree.root = BSTNode(2, BSTNode(1, None, None), BSTNode(7, None, None))
        self.assertEqual(is_empty(BTree), False)
        self.assertEqual(is_empty(BinarySearchTree(comes_before)), True)

    def test_insert_help(self):
        self.assertEqual(insert_help(BSTNode(8, BSTNode(4, None, None), BSTNode(12, None, None)),
        3, comes_before), BSTNode(8, BSTNode(4, BSTNode(3, None, None), None),
        BSTNode(12, None, None)))
        self.assertEqual(insert_help(BSTNode(8, BSTNode(4, None, None), BSTNode(12, None, None)),
        15, comes_before), BSTNode(8, BSTNode(4, None, None), BSTNode(12, None,
        BSTNode(15, None, None))))

    def test_insert(self):
        BTree = BinarySearchTree(comes_before)
        BTree = insert(BTree, 2)
        self.assertEqual(BTree.root, BSTNode(2,None,None))
        BTree.root = BSTNode(2, BSTNode(1, None, None), BSTNode(7, None, None))
        BTree = insert(BTree, 9)
        self.assertEqual(BTree.root, BSTNode(2, BSTNode(1, None, None), BSTNode(7, None,
        BSTNode(9, None, None))))
        BTree = BinarySearchTree(comes_before)
        BTree.root = BSTNode(2, BSTNode(1, None, None), BSTNode(7, None, None))
        BTree = insert(BTree, 1)
        self.assertEqual(BTree.root,  BSTNode(2, BSTNode(1, None, BSTNode(1, None, None)),
        BSTNode(7, None, None)))
        BTree = BinarySearchTree(comes_before)
        BTree.root = BSTNode(103, BSTNode(51, BSTNode(24, BSTNode(11, BSTNode(5, None,None),
        BSTNode(15, BSTNode(12, None, None), None)), BSTNode(37, BSTNode(28, None, None),
        BSTNode(43, None, None))),
        BSTNode(70, BSTNode(57, None, None), BSTNode(83, BSTNode(77, None, None),
        BSTNode(94, None, None)))), BSTNode(143, BSTNode(120, BSTNode(107, None, None),
        BSTNode(137, BSTNode(125, None, None),
        BSTNode(139, None, BSTNode(141, None, None)))), BSTNode(194, BSTNode(162,
        BSTNode(151, None, None), BSTNode(184, None, None)), BSTNode(210, None, None))))
        BTree = insert(BTree, 2)
        self.assertEqual(BTree.root, BSTNode(103, BSTNode(51, BSTNode(24, BSTNode(11,
        BSTNode(5, BSTNode(2, None, None),None), BSTNode(15, BSTNode(12, None, None), None)),
        BSTNode(37, BSTNode(28, None, None), BSTNode(43, None, None))),
        BSTNode(70, BSTNode(57, None, None), BSTNode(83, BSTNode(77, None, None),
        BSTNode(94, None, None)))), BSTNode(143, BSTNode(120, BSTNode(107, None, None),
        BSTNode(137, BSTNode(125, None, None), BSTNode(139, None,
        BSTNode(141, None, None)))), BSTNode(194, BSTNode(162, BSTNode(151, None, None),
        BSTNode(184, None, None)), BSTNode(210, None, None)))))
        BTree = insert(BTree, 59)
        self.assertEqual(BTree.root, BSTNode(103, BSTNode(51, BSTNode(24, BSTNode(11, BSTNode(5,
        BSTNode(2, None, None),None), BSTNode(15, BSTNode(12, None, None), None)),
        BSTNode(37, BSTNode(28, None, None), BSTNode(43, None, None))),
        BSTNode(70, BSTNode(57, None, BSTNode(59, None, None)), BSTNode(83,
        BSTNode(77, None, None), BSTNode(94, None, None)))), BSTNode(143, BSTNode(120,
        BSTNode(107, None, None), BSTNode(137, BSTNode(125, None, None),
        BSTNode(139, None, BSTNode(141, None, None)))), BSTNode(194, BSTNode(162,
        BSTNode(151, None, None), BSTNode(184, None, None)), BSTNode(210, None, None)))))
        BTree = insert(BTree, 101)
        self.assertEqual(BTree.root, BSTNode(103, BSTNode(51, BSTNode(24, BSTNode(11, BSTNode(5,
        BSTNode(2, None, None),None), BSTNode(15, BSTNode(12, None, None), None)), BSTNode(37,
        BSTNode(28, None, None), BSTNode(43, None, None))),
        BSTNode(70, BSTNode(57, None, BSTNode(59, None, None)), BSTNode(83,
        BSTNode(77, None, None), BSTNode(94, None, BSTNode(101, None, None))))),
        BSTNode(143, BSTNode(120, BSTNode(107, None, None), BSTNode(137,
        BSTNode(125, None, None),
        BSTNode(139, None, BSTNode(141, None, None)))), BSTNode(194, BSTNode(162,
        BSTNode(151, None, None), BSTNode(184, None, None)), BSTNode(210, None, None)))))
        BTree = insert(BTree, 145)
        self.assertEqual(BTree.root, BSTNode(103, BSTNode(51, BSTNode(24, BSTNode(11, BSTNode(5,
        BSTNode(2, None, None),None), BSTNode(15, BSTNode(12, None, None), None)), BSTNode(37,
        BSTNode(28, None, None), BSTNode(43, None, None))),
        BSTNode(70, BSTNode(57, None, BSTNode(59, None, None)), BSTNode(83,
        BSTNode(77, None, None), BSTNode(94, None, BSTNode(101, None, None))))), BSTNode(143,
        BSTNode(120, BSTNode(107, None, None), BSTNode(137, BSTNode(125, None, None),
        BSTNode(139, None, BSTNode(141, None, None)))), BSTNode(194, BSTNode(162, BSTNode(151,
        BSTNode(145, None, None), None), BSTNode(184, None, None)),
        BSTNode(210, None, None)))))
        BTree = insert(BTree, 215)
        self.assertEqual(BTree.root, BSTNode(103, BSTNode(51, BSTNode(24, BSTNode(11, BSTNode(5,
        BSTNode(2, None, None),None), BSTNode(15, BSTNode(12, None, None), None)), BSTNode(37,
        BSTNode(28, None, None), BSTNode(43, None, None))),
        BSTNode(70, BSTNode(57, None, BSTNode(59, None, None)), BSTNode(83,
        BSTNode(77, None, None), BSTNode(94, None, BSTNode(101, None, None))))),
        BSTNode(143, BSTNode(120, BSTNode(107, None, None), BSTNode(137,
        BSTNode(125, None, None),
        BSTNode(139, None, BSTNode(141, None, None)))), BSTNode(194, BSTNode(162,
        BSTNode(151, BSTNode(145, None, None), None), BSTNode(184, None, None)),
        BSTNode(210, None, BSTNode(215, None, None))))))

    def test_lookup(self):
        BTree = BinarySearchTree(comes_before)
        self.assertEqual(lookup(BTree, 6), False)
        BTree.root = BSTNode(2, BSTNode(1, None, None), BSTNode(7, None, None))
        self.assertEqual(lookup(BTree, 1), True)
        self.assertEqual(lookup(BTree,12), False)

    def test_lookup_help(self):
        self.assertEqual(lookup_help(BSTNode(15, BSTNode(7, None, BSTNode(11, None, None)),
        BSTNode(24, BSTNode(18, None, None), BSTNode(37, None, None))), 7, comes_before), True)
        self.assertEqual(lookup_help(BSTNode(15, BSTNode(7, None, BSTNode(11, None, None)),
        BSTNode(24, BSTNode(18, None, None), BSTNode(37, None, None))), 37, comes_before), True)
        self.assertEqual(lookup_help(BSTNode(15, BSTNode(7, None, BSTNode(11, None, None)),
        BSTNode(24, BSTNode(18, None, None), BSTNode(37, None, None))), 27, comes_before), False)
        self.assertEqual(lookup_help(BSTNode(15, BSTNode(7, None, BSTNode(11, None, None)),
        BSTNode(24, BSTNode(18, None, None), BSTNode(37, None, None))), 11, comes_before), True)

    def test_delete(self):
        BTree = BinarySearchTree(comes_before)
        self.assertEqual(delete(BTree, 1), BTree)
        self.assertEqual(BTree.root, None)
        self.assertEqual(BTree, BinarySearchTree(comes_before))

        BTree = BinarySearchTree(comes_before)
        BTree.root = BSTNode(7, BSTNode(3, BSTNode(1, None, BSTNode(5, None, None)),
        BSTNode(5, None, None)), BSTNode(12, BSTNode(9, None, None), BSTNode(17, None, None)))
        BTree = delete(BTree, 17)
        self.assertEqual(BTree.root, BSTNode(7, BSTNode(3, BSTNode(1, None,
        BSTNode(5, None, None)), BSTNode(5, None, None)), BSTNode(12,
        BSTNode(9, None, None), None)))

        BTree = BinarySearchTree(comes_before)
        BTree.root = BSTNode(7, BSTNode(3, BSTNode(1, None, BSTNode(5, None, None)),
        BSTNode(5, None, None)), BSTNode(12, BSTNode(9, None, None), BSTNode(17, None, None)))
        BTree = delete(BTree, 31)
        BTree = delete(BTree, 97)
        self.assertEqual(BTree.root, BSTNode(7, BSTNode(3, BSTNode(1, None,
        BSTNode(5, None, None)), BSTNode(5, None, None)), BSTNode(12, BSTNode(9, None, None),
        BSTNode(17, None, None))))

        BTree = BinarySearchTree(comes_before)
        BTree.root = BSTNode(7, BSTNode(3, BSTNode(1, None, BSTNode(5, None, None)),
        BSTNode(5, None, None)), BSTNode(12, None, BSTNode(17, None, None)))
        BTree = delete(BTree, 12)
        self.assertEqual(BTree.root, BSTNode(7, BSTNode(3, BSTNode(1, None,
        BSTNode(5, None, None)), BSTNode(5, None, None)), BSTNode(17, None, None)))

        BTree = BinarySearchTree(comes_before)
        BTree.root = BSTNode(7, BSTNode(3, BSTNode(1, None, BSTNode(5, None, None)),
        BSTNode(5, None, None)), BSTNode(12, BSTNode(9, None, None), None))
        BTree = delete(BTree, 12)
        self.assertEqual(BTree.root, BSTNode(7, BSTNode(3, BSTNode(1, None,
        BSTNode(5, None, None)), BSTNode(5, None, None)), BSTNode(9, None, None)))

        BTree = BinarySearchTree(comes_before)
        BTree.root = BSTNode(7, BSTNode(3, BSTNode(1, None, BSTNode(5, None, None)),
        BSTNode(6, None, None)), BSTNode(12, BSTNode(9, None, None), BSTNode(17, None, None)))
        BTree = delete(BTree, 3)
        self.assertEqual(BTree.root, BSTNode(7, BSTNode(6, BSTNode(1, None,
        BSTNode(5, None, None)), None), BSTNode(12, BSTNode(9, None, None),
        BSTNode(17, None, None))))

        BTree = BinarySearchTree(comes_before)
        BTree.root = BSTNode(8, BSTNode(3, BSTNode(1, None, BSTNode(5, None, None)),
        BSTNode(7, BSTNode(6, None, None), None)), BSTNode(12, BSTNode(9, None, None),
        BSTNode(17, None, None)))
        BTree = delete(BTree, 3)
        self.assertEqual(BTree.root, BSTNode(8, BSTNode(6, BSTNode(1, None,
        BSTNode(5, None, None)), BSTNode(7, None, None)), BSTNode(12, BSTNode(9, None, None),
        BSTNode(17, None, None))))

    def test_find_min(self):
        self.assertEqual(find_min(None, None), (None, None))
        self.assertEqual(find_min(BSTNode(7, None, None), BSTNode(2, BSTNode(1, None, None),
        BSTNode(7, None, None))), (BSTNode(2, BSTNode(1, None, None), BSTNode(7, None, None)),
        BSTNode(7, None, None)))

if __name__ == '__main__':
    unittest.main()
