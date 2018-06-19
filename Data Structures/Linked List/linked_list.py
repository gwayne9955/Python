# a List is one of
#   - None, or
#   - Pair(first, rest)
class Pair:
    def __init__(self, first, rest):
        self.first = first  # A HuffmanTree
        self.rest = rest    # An List

    def __eq__(self, other):
        return (type(other) == Pair
                and self.first == other.first
                and self.rest == other.rest)

    def __repr__(self):
        return "Pair({!r}, {!r})".format(self.first, self.rest)

# () -> List
# This function takes no arguments and returns an empty list
def empty_list():
    return None

# List int HuffmanTree -> List
# This function takes a list, an integer index, and another value (of any type) as arguments and
# places the value at index position in the list (zero-based indexing; any element at the given
# index before this operation will now immediately follow the new element)
def add(lister, index, value):
    if (index != 0 and lister == None) or index < 0:
        raise IndexError()
    else:
        if index == 0:
            return Pair(value, lister)
        else:
            return Pair(lister.first, add(lister.rest, index - 1, value))

# List-> int
# Determines the length of the list
def length(lister):
    if lister == None:
        return 0
    else:
        return 1 + length(lister.rest)

# List int -> HuffmanTree
# Returns the value in the list at the given index
def get(lister, index):
    if lister == None or index < 0:
        raise IndexError()
    else:
        if index == 0:
            return lister.first
        else:
            return get(lister.rest, index - 1)

# List int HuffmanTree -> List
# Replaces the element at index position in the list with the given value and returns the list
def set(lister, index, value):
    if lister == None or index < 0:
        raise IndexError()
    else:
        if index == 0:
            return Pair(value, lister.rest)
        else:
            return Pair(lister.first, set(lister.rest, index - 1, value))

# List int -> HuffmanTree List
# Removes the value at the given index and returns the value removed and the list
def remove(lister, index, pos = 0, partial = None):
    if (index < 0):
        raise IndexError()
    else:
        if (lister == None):
            raise IndexError()
        if (index == pos):
            completeList = lister.rest
            while (partial != None):
                completeList = add(completeList, index - pos, partial.first)
                pos = pos - 1
                partial = partial.rest
            return (lister.first, completeList)
        else:
            return remove(lister.rest, index, pos + 1, add(partial, pos, lister.first))

# List function -> None
# Applies the provided function to the value at each position in the List (from left-to-right)
def foreach(lister, function):
    if lister == None:
        # print("")
        return None
    else:
        function(lister.first)
        return foreach(lister.rest, function)

# List HuffmanTree -> List
# Accepts a SORTED linked list and a given value and returns a new list
# with the value inserted into the list in the proper location
def insert_sorted(lister, tree, function):
    if lister == None:
        return Pair(tree, None)
    else:
        if function(tree, lister.first):
            return Pair(tree, Pair(lister.first, lister.rest))
        else:
            return Pair(lister.first, insert_sorted(lister.rest, tree, function))

# List function -> List
# Sorts the List such that the elements are in ascending order as determined by the
# "less-than" function
def sort(lister, function, partial = None):
    if lister == None:
        return partial
    else:
        partial = insert_sorted(partial, lister.first, function)
        return sort(lister.rest, function, partial)
