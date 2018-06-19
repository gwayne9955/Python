# A Stack is a class that represents an Array style stack in python
class Stack:
    def __init__(self):
        self.array = [None] * 5 # a stack of Any's
        self.size = 0           # a number
        self.capacity = 5       # a number

    def __eq__(self, other):
        if (type(other) != Stack or self.size != other.size):
            return False
        else:
            for i in range(0, self.size):
                if self.array[i] != other.array[i]:
                    return False
            return True
        #loop all elements regardless of capacity and returns true if all are equal still

    def __repr__(self):
        return "Stack({!r}, {!r}, {!r})".format(self.array, self.size, self.capacity)

# () -> Stack
# This function takes no arguments and returns an empty stack
def empty_stack():
    return Stack()

# Stack Any -> Stack
# This function takes a Stack and another value (of any type) as arguments and
# places the value at top position in the Stack
def push(stack, value):
    if size(stack) == stack.capacity:
        grow(stack)
    stack.array[size(stack)] = value
    stack.size = stack.size + 1
    return stack

# Stack -> Any Stack
# Removes the top value and returns the value removed and the stack
def pop(stack):
    if size(stack) == 0:
        raise IndexError()
    else:
        sizer = size(stack)
        old = stack.array[sizer - 1]
        stack.array[sizer - 1] = None
        stack.size = stack.size - 1
        return (old, stack)

# Stack int -> Any
# Returns the value in the stack at the top
def peek(stack):
    if size(stack) == 0:
        raise IndexError()
    else:
        return stack.array[stack.size - 1]

# Stack -> int
# Determines the size of the stack
def size(stack):
    return stack.size

# Stack -> bool
# Returns True if the Stack is empty, false otherwise
def is_empty(stack):
    if size(stack) == 0:
        return True
    else:
        return False

# Stack -> None
# Grows the stack by mutating its array, doubling its capacity, and copying each value over
def grow(stacker):
    stacker_2 = Stack()
    stacker_2.array = [None] * stacker.capacity * 2
    stacker_2.size = stacker.size
    stacker_2.capacity = stacker.capacity * 2
    for i in range(0, stacker.capacity):
        stacker_2.array[i] = stacker.array[i]
    stacker.capacity = stacker.capacity * 2
    stacker.array = stacker_2.array
