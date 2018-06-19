import sys
sys.setrecursionlimit(50100)
# A PriorityQueue is a class that contains a function and a List
class PriorityQueue:
    def __init__(self, comes_before):
        self.comes_before = comes_before    # a function
        self.list = None                    # a list
        self.size = 0                       # a int

    def __eq__(self, other):
        return (type(other) == PriorityQueue
                and self.comes_before == other.comes_before
                and self.list == other.list)

    def __repr__(self):
        return "PriorityQueue({!r}, {!r})".format(self.comes_before.__name__, self.list)

# a List is one of
#   - None, or
#   - Pair(first, rest)
class Pair:
    def __init__(self, first, rest):
        self.first = first  # A Value
        self.rest = rest    # A List

    def __eq__(self, other):
        return (type(other) == Pair
                and self.first == other.first
                and self.rest == other.rest)

    def __repr__(self):
        return "Pair({!r}, {!r})".format(self.first, self.rest)

# Any Any -> bool
# returns true if value one comes before value two
def comes_before(val_1, val_2):
    return val_1 < val_2

# function -> List
# This function takes no arguments and returns an empty list
def empty_pqueue(function):
    return PriorityQueue(function)

# List Value -> List
# Accepts a SORTED linked list and a given value and returns a new list
# with the value inserted into the list in the proper location
def insert(lister, value, function):
    if lister == None:
        return Pair(value, None)
    else:
        if function(value, lister.first):
            return Pair(value, Pair(lister.first, lister.rest))
        else:
            return Pair(lister.first, insert(lister.rest, value, function))

# PriorityQueue Value -> PriorityQueue
# Adds a value to the PriorityQueue in the correct location based on the comes_before
def enqueue(pq, value):
    pq.list = insert(pq.list, value, pq.comes_before)
    pq.size += 1
    return pq

# PriorityQueue -> (Value, PriorityQueue)
# Removes the top value and returns the value removed and the PriorityQueue
def dequeue(pq):
    if pq.list is None:
        raise IndexError()
    else:
        val = pq.list.first
        pq.list = pq.list.rest
        pq.size -= 1
        return (val, pq)

# PriorityQueue -> Any
# Returns the value in the PriorityQueue with the highest priority
def peek(pq):
    if pq.list is None:
        raise IndexError()
    else:
        return pq.list.first

# PriorityQueue -> int
# Determines the length of the PriorityQueue
def size(pq):
    return pq.size

# PriorityQueue -> bool
# Returns True if the PriorityQueue is empty, false otherwise
def is_empty(pq):
    if pq.list is None:
        return True
    else:
        return False
