#
# Garrett Wayne
#

# a Stack is one of
#   - None, or
#   - Pair(first, rest)
class Pair:
    def __init__(self, first, rest):
        self.first = first  # An Any
        self.rest = rest    # A Stack

    def __eq__(self, other):
        return (type(other) == Pair
                and self.first == other.first
                and self.rest == other.rest)

    def __repr__(self):
        return "Pair({!r}, {!r})".format(self.first, self.rest)

# () -> Stack
# This function takes no arguments and returns an empty stack
def empty_stack():
    return None

# Stack Any -> Stack
# This function takes a Stack and another value (of any type) as arguments and
# places the value at top position in the Stack
def push(stack, value):
    return Pair(value, stack)

# Stack -> Any Stack
# Removes the top value and returns the value removed and the stack
def pop(stack):
    if stack is None:
        raise IndexError()
    else:
        return (stack.first, stack.rest)

# Stack -> Any
# Returns the value in the stack at the top
def peek(stack):
    if stack is None:
        raise IndexError()
    else:
        return stack.first

# Stack -> int
# Determines the length of the stack
def size(stack):
    if stack == None:
        return 0
    else:
        return 1 + size(stack.rest)

# Stack -> bool
# Returns True if the Stack is empty, false otherwise
def is_empty(stack):
    if stack is None:
        return True
    else:
        return False
