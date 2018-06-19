#
# Garrett Wayne
#

# A Queue is a class that represents an Array style queue in python
class Queue:
    def __init__(self):
        self.array = [None] * 5000  # a List
        self.front = 0              # a number
        self.back = 0               # a number
        self.size = 0               # a number

    def __eq__(self, other):
        return (type(other) == Queue
                and self.array == other.array
                and self.front == other.front
                and self.back == other.back
                and self.size == other.size)

    def __repr__(self):
        return "Queue({!r}, {!r}, {!r}, {!r})".format(self.array, self.front, self.back, self.size)

# () -> Queue
# This function takes no arguments and returns an empty queue
def empty_queue():
    return Queue()

# Queue Any -> Queue
# Adds the value to the back of the queue, returning the queue
def enqueue(q, value):
    if q.size == 5000:
        raise IndexError
    elif q.back == 4999: # wrapping around
        q.array[0] = value
        q.back = 0
        q.size += 1
        return q
    elif q.size == 0:
        q.array[q.back] = value
        q.size += 1
        return q
    else:
        q.array[q.back + 1] = value
        q.back += 1
        q.size += 1
        return q

# Queue -> (Any, Queue)
# Removes the front value from the queue and returns the value removed and the queue
def dequeue(q):
    if q.size == 0:
        raise IndexError
    else:
        val = q.array[q.front]
        if q.front == 4999:
            q.front = 0
        elif q.size != 1:
            q.front += 1
        q.size -= 1
        return val, q

# Queue -> Any
# Returns the value at the front of the queue
def peek(q):
    if q.size == 0:
        raise IndexError
    else:
        return q.array[q.front]

# Queue -> int
# Returns the number of elements in the queue
def size(q):
    return q.size

# Queue -> bool
# Returns True if the queue is empty, false otherwise
def is_empty(q):
    if q.size == 0:
        return True
    else:
        return False
