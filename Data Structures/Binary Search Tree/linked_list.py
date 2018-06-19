#
# Garrett Wayne
#

# an AnyList is one of
#   - None, or
#   - Pair(first, rest)
class Pair:
    def __init__(self, first, rest):
        self.first = first  # An Any
        self.rest = rest    # An AnyList

    def __eq__(self, other):
        return (type(other) == Pair
                and self.first == other.first
                and self.rest == other.rest)

    def __repr__(self):
        return "Pair({!r}, {!r})".format(self.first, self.rest)

class Iterator:
    def __init__(self, lst):
        self.lst = lst # an AnyList

    def __eq__(self, other):
        return (type(other) == Iterator
                and self.lst == other.lst)
    def __repr__(self):
        return "Iterator({!r})".format(self.lst)

# () -> AnyList
# This function takes no arguments and returns an empty list
def empty_list():
    return None

# AnyList int Any -> AnyList
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

# AnyList-> int
# Determines the length of the list
def length(lister):
    if lister == None:
        return 0
    else:
        return 1 + length(lister.rest)

# AnyList int -> Any
# Returns the value in the list at the given index
def get(lister, index):
    if lister == None or index < 0:
        raise IndexError()
    else:
        if index == 0:
            return lister.first
        else:
            return get(lister.rest, index - 1)

# AnyList int Any -> AnyList
# Replaces the element at index position in the list with the given value and returns the list
def set(lister, index, value):
    if lister == None or index < 0:
        raise IndexError()
    else:
        if index == 0:
            return Pair(value, lister.rest)
        else:
            return Pair(lister.first, set(lister.rest, index - 1, value))

# AnyList int -> Any AnyList
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
        print("")
        return None
    else:
        function(lister.first)
        return foreach(lister.rest, function)

# List Any -> List
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

# List function -> List
# Sorts the List such that the elements are in ascending order as determined by the
# "less-than" function
def sort(lister, function, partial = None):
    if lister == None:
        return partial
    else:
        partial = insert(partial, lister.first, function)
        return sort(lister.rest, function, partial)

# List -> Iterator
# Returns an Iterator with the given List
def object_iterator(lister):
    new_it = Iterator(lister)
    return new_it

# Iterator -> bool
# Returns true if there is another value to return from the iterated list
def has_next(it):
    if it.lst is None:
        return False
    elif it.lst.first is None:
        return False
    else:
        return True

# Iterator -> Any
# Return the next element of the iterator
def next(it):
    if it.lst is None:
        raise StopIteration
    else:
        val = it.lst.first
        it.lst = it.lst.rest
        return val

# List -> Any
# Yields each value in the List
def yield_iterator(lister):
    if lister is not None:
        yield lister.first
        yield from yield_iterator(lister.rest)
