class BinarySearchTree:
    def __init__(self, comes_before):
        self.comes_before = comes_before    # a function
        self.root = None                    # a BST

    def __eq__(self, other):
        return (type(other) == BinarySearchTree
                and self.comes_before == other.comes_before
                and self.root == other.root)

    def __repr__(self):
        return "BinarySearchTree({!r}, {!r})".format(self.comes_before.__name__, self.root)

# A BST is one of
#   - None, or
#   - BSTNode(value, left, right) where numbers in left < value,
#   numbers in right are not
class BSTNode:
    def __init__(self, value, left, right):
        self.value = value  # an Any
        self.left = left    # a BST
        self.right = right  # a BST

    def __eq__(self, other):
        return (type(other) == BSTNode
                and self.value == other.value
                and self.left == other.left
                and self.right == other.right)

    def __repr__(self):
        return ("BSTNode({!r}, {!r}, {!r})".format(self.value, self.left, self.right))

# BST -> bool
# Returns if the tree is empty or not
def is_empty(tree):
    if tree.root is None:
        return True
    else:
        return False

# Any Any -> bool
# returns true if value one comes before value two
def comes_before(val_1, val_2):
    return val_1 < val_2

# BinarySearchTree Any -> BinarySearchTree
# Inserts the value into the correct spot in the tree
def insert(bst, value):
    if bst.root is None:
        bst.root = BSTNode(value, None, None)
        return bst
    else:
        bst.root = insert_help(bst.root, value, bst.comes_before)
        return bst

# BST Any function -> BST
# Deals only in BST instead of wrapper class
def insert_help(tree, value, comparator):
    if tree is None:
        return BSTNode(value, None, None)
    else:
        if comparator(value, tree.value):
            return BSTNode(tree.value, insert_help(tree.left, value, comparator), tree.right)
        else:
            return BSTNode(tree.value, tree.left, insert_help(tree.right, value, comparator))

# BinarySearchTree Any -> bool
# Determines if the given value is in the tree
def lookup(bst, value):
    if bst.root is None:
        return False
    else:
        return lookup_help(bst.root, value, bst.comes_before)

# BST Any function -> bool
# Deals only in BST instead of wrapper class
def lookup_help(tree, value, comparator):
    if tree is None:
        return False
    else:
        if value == tree.value:
            return True
        elif comparator(value, tree.value):
            return lookup_help(tree.left, value, comparator)
        else:
            return lookup_help(tree.right, value, comparator)

# BinarySearchTree Any -> BinarySearchTree
# Removes the value from the tree if postsent, returning the resulting Binary Search Tree
def delete(bst, value):
    if bst.root is None:
        return bst
    else:
        bst.root = delete_help(bst.root, value, bst.comes_before)
        return bst

# BST Any function -> BST
# Deals only in BST instead of wrapper class
def delete_help(tree, value, comparator):
    if tree.value == value:
        if tree.left is not None and tree.right is not None:
            parent_successor, successor = find_min(tree.right, tree)
            if parent_successor.left == successor:
                parent_successor.left = successor.right
            else:
                parent_successor.right = successor.right
            successor.left = tree.left
            successor.right = tree.right
            return successor
        else:
            if tree.left is not None:
                return tree.left
            else:
                return tree.right
    else:
        if comparator(value, tree.value):
            if tree.left is not None:
                tree.left = delete_help(tree.left, value, comparator)
            # else the key is not in the tree, do nothing
        else:
            if tree.right is not None:
                tree.right = delete_help(tree.right, value, comparator)
    return tree

# BST BST -> (BST, BST)
# return the minimum node in the current tree and its parent.
# The parent node is passed in as an argument
# so that eventually when the leftmost child is reached, the
# call can return both the parent to the successor and the successor
def find_min(tree, parent):
    if parent is None:
        return None, None
    elif tree.left is not None:
        return find_min(tree.left, tree)
    else:
        return parent, tree

# BinarySearchTree -> Any
# Returns an iterator (using yield) of the elements in postfix order wherein, for a given node,
# the node is visited before its children (visit the left child before the right child)
def prefix_iterator(bst):
    yield from prefix_iterator_help(bst.root)

# BST -> BST
# Deals only in BST instead of wrapper class
def prefix_iterator_help(tree):
    if tree is not None:
        yield tree.value                            # give them the value which is one thing
        yield from prefix_iterator_help(tree.left)  # gives them the yeilding that happens inside
                                                    # of the left, not just one thing (a BSTNode)
        yield from prefix_iterator_help(tree.right) # gives them the yeilding that happens inside
                                                    # of the right, not just one thing (a BSTNode)

# BinarySearchTree -> Any
# Returns an iterator (using yield) of the elements in infix order wherein, for a given node,
# the node is visited after its left child but before its right child
def infix_iterator(bst):
    yield from infix_iterator_help(bst.root)

# BST -> BST
# Deals only in BST instead of wrapper class
def infix_iterator_help(tree):
    if tree is not None:
        yield from infix_iterator_help(tree.left)   # gives them the yeilding that happens inside
                                                    # of the left, not just one thing (a BSTNode)
        yield tree.value                            # give them the value which is one thing
        yield from infix_iterator_help(tree.right)  # gives them the yeilding that happens inside
                                                    # of the right, not just one thing (a BSTNode)

# BinarySearchTree -> Any
# Returns an iterator (using yield) of the elements in postfix order wherein, for a given node,
# the node is visited before its children
def postfix_iterator(bst):
    yield from postfix_iterator_help(bst.root)

# BST -> BST
# Deals only in BST instead of wrapper class
def postfix_iterator_help(tree):
    if tree is not None:
        yield from postfix_iterator_help(tree.left) # gives them the yeilding that happens inside
                                                    # of the left, not just one thing (a BSTNode)
        yield from postfix_iterator_help(tree.right)# gives them the yeilding that happens inside
                                                    # of the right, not just one thing (a BSTNode)
        yield tree.value                            # give them the value which is one thing
