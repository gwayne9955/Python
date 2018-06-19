import sys
sys.setrecursionlimit(10100)
from linked_list import *

# a ListQueue is an object that contains two Linked Lists
class ListQueue:
    def __init__(self):
        self.forward = None     # a List
        self.backward = None    # a List

    def __eq__(self, other):
        return (type(other) == ListQueue
                and self.forward == other.forward
                and self.backward == other.backward)

    def __repr__(self):
        return "ListQueue({!r}, {!r})".format(self.forward, self.backward)

# () -> ListQueue
# This function takes no arguments and returns an empty queue
def empty_queue():
    return ListQueue()

# ListQueue Any -> ListQueue
# Adds the value to the back of the queue, returning the queue
def enqueue(q, value):
    q.backward = add(q.backward, 0, value)
    return q

# ListQueue -> (Any, ListQueue)
# Removes the front value from the queue and returns the value removed and the queue
def dequeue(q):
    if q.forward is None and q.backward is None:
        raise IndexError
    elif q.forward is None:
        q.forward = reverse(q.backward)
        q.backward = None
        val = q.forward.first
        q.forward = q.forward.rest
        return val, q
    else:
        val = q.forward.first
        q.forward = q.forward.rest
        return val, q

# ListQueue -> Any
# Returns the value at the front of the queue
def peek(q):
    if q.forward is None and q.backward is None:
        raise IndexError
    elif q.forward is None:
        q.forward = reverse(q.backward)
        q.backward = None
        val = q.forward.first
        return val
    else:
        val = q.forward.first
        return val

# ListQueue -> int
# Returns the number of elements in the queue
def size(q):
    return length(q.forward) + length(q.backward)

# ListQueue -> bool
# Returns True if the queue is empty, false otherwise
def is_empty(q):
    if q.forward is None and q.backward is None:
        return True
    else:
        return False

# Stack -> Stack
# Reverses the given Stack and returns the resulting Stack
def reverse(backward, forward = None):
    if backward is None:
        return forward
    else:
        next_pair = backward.rest
        backward.rest = forward
        forward = backward
        backward = next_pair
        return reverse(backward, forward)
