# A Red/BlackTree is one of
#   - None, or
#   - Node(Color, float, Red/BlackTree, Red/BlackTree)

class Node:
    def __init__(self, color, left, right):
        self.color = color
        self.left = left
        self.right = right

# A Color is one of
#   - "R" or
#   - "B"

# Red/BlackTree float -> Red/BlackTree
# inserts the value in the tree returning the tree (forcing the root to be black)
def insert(tree, val):
    t = insert2(tree, val)
    return Node("B", t.val, t.left, t.right)

# Red/BlackTree float -> Red/BlackTree
# insert the value into the tree
def insert2(tree, val):
    if tree is None:
        return Node("R", val, None, None) # try to insert a red Node, rebalance other nodes if necessary
    else:
        if val < tree.val:
            return rebalance(Node(tree.color, tree.val, insert2(tree.left, val), tree.right))
        else:
            return rebalance(Node(tree.color, tree.val, tree.left, insert2(tree.right, val)))

# Node -> Node
# Rebalance a tree with a chain of two red nodes below a black node
def rebalance(tree):
    # first check to see if the tree is a black node with two red nodes as children
    # then check to see what case you are in (out of the 4 cases)
    if (tree.color == "B" and tree.left is not None and tree.left.color == "R" and tree.left.left is not None and tree.left.left.color =="R"):
        return Node("R", tree.left.value,
                                Node("B", tree.left.left.val, tree.left.left.left, tree.left.left.right),
                                Node("B", tree.val, tree.left.right, tree.right))
    elif (tree.color == "B" and tree.left is not None and tree.left.color == "R" and tree.left.right is not None and tree.left.right.color =="R"):
        return Node("R", tree.left.right.value,
                                Node("B", tree.left.val, tree.left.left, tree.left.right.left),
                                Node("B", tree.val, tree.left.right.right, tree.right))
    elif (tree.color == "B" and tree.right is not None and tree.right.color == "R" and tree.right.left is not None and tree.right.left.color =="R"):
        return Node("R", tree.right.left.value,
                                Node("B", tree.val, tree.left, tree.right.left.left),
                                Node("B", tree.right.val, tree.right.left.right, tree.right.right))
    elif (tree.color == "B" and tree.right is not None and tree.right.color == "R" and tree.right.right is not None and tree.right.right.color =="R"):
        return Node("R", tree.right.value,
                                Node("B", tree.val, tree.left, tree.right.left),
                                Node("B", tree.right.right.val, tree.right.right.left, tree.right.right.right))
    else:
        return tree

