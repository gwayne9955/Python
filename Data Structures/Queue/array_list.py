# A List is a class that represents an Array style list in python
class List:
    def __init__(self):
        self.array = [None] * 5 # a list of Songs
        self.length = 0         # a number
        self.capacity = 5       # a number

    def __eq__(self, other):
        if (type(other) != List or self.length != other.length):
            return False
        else:
            for i in range(0, self.length):
                if self.array[i] != other.array[i]:
                    return False
            return True
        #loop all elements regardless of capacity and returns true if all are equal still

    def __repr__(self):
        return "List({!r}, {!r}, {!r})".format(self.array, self.length, self.capacity)

# () -> List
# This function takes no arguments and returns an empty list
def empty_list():
    return List()

# List int Song -> List
# This function takes a list, an integer index, and another value (of any type) as arguments and
# places the value at index position in the list (zero-based indexing; any element at the given
# index before this operation will now immediately follow the new element)
def add(lister, index, value):
    if index < 0 or index > length(lister):
        raise IndexError()
    else:
        if length(lister) == lister.capacity:
            grow(lister)
        if index >= length(lister):
            lister.array[index] = value
            lister.length = lister.length + 1
        else:
            for i in range(length(lister), index, -1):
                lister.array[i] = lister.array[i - 1]
            lister.array[index] = value
            lister.length = lister.length + 1
        return lister

# List -> int
# Determines the length of the list
def length(lister):
    return lister.length

# List int -> Song
# Returns the value in the list at the given index
def get(lister, index):
    if index < 0 or index >= length(lister):
        raise IndexError()
    else:
        return lister.array[index]

# List int Song -> List
# Replaces the element at index position in the list with the given value and returns the list
def set(lister, index, value):
    if index < 0 or index >= length(lister):
        raise IndexError()
    else:
        lister.array[index] = value
        return lister

# List int -> Song List
# Removes the value at the given index and returns the value removed and the list
def remove(lister, index):
    if index < 0 or index >= length(lister):
        raise IndexError()
    else:
        old = lister.array[index]
        for i in range(index, length(lister) - 1):
            lister.array[i] = lister.array[i + 1]
        lister.array[length(lister) - 1] = None
        lister.length = lister.length - 1
        return (old, lister)

# List -> None
# Grows the list by mutating its array, doubling its capacity, and copying each value over
def grow(lister):
    lister_2 = List()
    lister_2.array = [None] * lister.capacity * 2
    lister_2.length = lister.length
    lister_2.capacity = lister.capacity * 2
    for i in range(0, lister.capacity):
        lister_2.array[i] = lister.array[i]
    lister.capacity = lister.capacity * 2
    lister.array = lister_2.array

# # List -> None
# # Grows the list by mutating its array, doubling its capacity, and copying each value over
# def grow(lister):
#     lister_2 = List()
#     lister_2.array = [None] * (lister.capacity + 1)
#     lister_2.length = lister.length
#     lister_2.capacity = lister.capacity + 1
#     for i in range(0, lister.capacity):
#         lister_2.array[i] = lister.array[i]
#     lister.capacity = lister.capacity + 1
#     lister.array = lister_2.array

# # List -> None
# # Grows the list by mutating its array, doubling its capacity, and copying each value over
# def grow(lister):
#     lister_2 = List()
#     lister_2.array = [None] * int(lister.capacity * 1.125 + 9)
#     lister_2.length = lister.length
#     lister_2.capacity = int(lister.capacity * 1.125 + 9)
#     for i in range(0, lister.capacity):
#         lister_2.array[i] = lister.array[i]
#     lister.capacity = int(lister.capacity * 1.125 + 9)
#     lister.array = lister_2.array

# List function -> None
# Applies the provided function to the value at each position in the List (from left-to-right)
def foreach(lister, function):
    for i in range(length(lister)):
        function(lister.array[i])
    # print("")
    return None

# List function -> List
# Sorts the List such that the elements are in ascending order as determined by the
# "less-than" function
def sort(lister, function):
    for index in range(1, length(lister)):
        currentvalue = lister.array[index]
        position = index
        while position > 0 and (function(currentvalue, lister.array[position - 1])):
            lister.array[position] = lister.array[position - 1]
            position = position - 1
        lister.array[position] = currentvalue
    return lister
