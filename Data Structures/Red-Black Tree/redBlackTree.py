#
# Garrett Wayne
#

# A Red/BlackTree is one of
#   - None, or
#   - Node(Color, value, Red/BlackTree, Red/BlackTree)
class Node:
    def __init__(self, color, val, left, right):
        self.color = color
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (type(other) == Node
                and self.color == other.color
                and self.val == other.val
                and self.left == other.left
                and self.right == other.right)

    def __repr__(self):
        return "Node({!r}, {!r}, {!r}, {!r})".format(self.color, self.val, self.left, self.right)

# A Color is one of
#   - "R" or
#   - "B"

# Red/BlackTree -> bool
# Returns if the tree is empty or not
def is_empty(tree):
    if tree is None:
        return True
    else:
        return False

# Red/BlackTree float -> Red/BlackTree
# inserts the value in the tree returning the tree (forcing the root to be black)
def insert(tree, val):
    t = insert_help(tree, val)
    return Node("B", t.val, t.left, t.right)

# Red/BlackTree float -> Red/BlackTree
# insert the value into the tree
def insert_help(tree, val):
    if tree is None:
        return Node("R", val, None, None) # try to insert a red Node, rebalance other nodes if necessary
    else:
        if val < tree.val:
            return rebalance(Node(tree.color, tree.val, insert_help(tree.left, val), tree.right))
        else:
            return rebalance(Node(tree.color, tree.val, tree.left, insert_help(tree.right, val)))

# Node -> Node
# Rebalance a tree with a chain of two red nodes below a black node
def rebalance(tree):
    # first check to see if the tree is a black node with two red nodes as children
    # then check to see what case you are in (out of the 4 cases)
    if (tree.color == "B" and tree.left is not None and tree.left.color == "R" and tree.left.left is not None and tree.left.left.color =="R"):
        return Node("R", tree.left.val,
                                Node("B", tree.left.left.val, tree.left.left.left, tree.left.left.right),
                                Node("B", tree.val, tree.left.right, tree.right))
    elif (tree.color == "B" and tree.left is not None and tree.left.color == "R" and tree.left.right is not None and tree.left.right.color =="R"):
        return Node("R", tree.left.right.val,
                                Node("B", tree.left.val, tree.left.left, tree.left.right.left),
                                Node("B", tree.val, tree.left.right.right, tree.right))
    elif (tree.color == "B" and tree.right is not None and tree.right.color == "R" and tree.right.left is not None and tree.right.left.color =="R"):
        return Node("R", tree.right.left.val,
                                Node("B", tree.val, tree.left, tree.right.left.left),
                                Node("B", tree.right.val, tree.right.left.right, tree.right.right))
    elif (tree.color == "B" and tree.right is not None and tree.right.color == "R" and tree.right.right is not None and tree.right.right.color =="R"):
        return Node("R", tree.right.val,
                                Node("B", tree.val, tree.left, tree.right.left),
                                Node("B", tree.right.right.val, tree.right.right.left, tree.right.right.right))
    else:
        return tree

# Red/BlackTree float -> bool
# Traverses the tree to lookup the value, returning true if the value is in the tree, false otherwise
def lookup(tree, val):
    if tree is None:
        return False
    elif tree.val == val:
        return True
    elif val < tree.val:
        return lookup(tree.left, val)
    elif val > tree.val:
        return lookup(tree.right, val)

# Red/BlackTree float -> Red/BlackTree
# Deletes the given element in the tree, rebalances the tree thereafter, and returns the tree (forcing the root node to be black)
def delete(tree, val):
    t = delete_help(tree, val)
    if t is None:
        return t
    return Node("B", t.val, t.left, t.right)

# Red/BlackTree float -> Red/BlackTree
# Deletes the given element in the tree, rebalances the tree thereafter, and returns the tree
def delete_help(tree, val):
    if tree is None:
        return tree
    else:
        if tree.val == val:
            if tree.left is not None and tree.right is not None:
                # Find min element right of current node
                parent_successor, successor = find_min(tree.right, tree)
                if parent_successor.left == successor:
                    parent_successor.left = successor.right
                else:
                    parent_successor.right = successor.right
                successor.left = tree.left
                successor.right = tree.right
                return successor
            elif tree.left is not None:
                return tree.left
            elif tree.right is not None:
                return tree.right
            else:
                return None
        elif val < tree.val:
            return rebalance(Node(tree.color, tree.val, delete_help(tree.left, val), tree.right))
        else:
            return rebalance(Node(tree.color, tree.val, tree.left, delete_help(tree.right, val)))

# Node Node -> (Node, Node)
# Return the minimum node in the current tree and its parent.
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
