#
# Garrett Wayne
#

# A HashTable has a 2D Python list, a capacity, a size, and a number of total collisions
class HashTable:
    def __init__(self):
        self.table = a = [[] for y in range(8)]     # A 2D Python list
        self.capacity = 8                           # An int
        self.size = 0                               # An int
        self.collisions = 0                         # An int

    def __eq__(self, other):
        return (type(other) == HashTable
                and self.table == other.table
                and self.capacity == other.capacity
                and self.size == other.size
                and self.collisions == other.collisions)

    def __repr__(self):
        return "HashTable({!r}, {!r}, {!r}, {!r})".format(self.table, self.capacity, self.size,
                self.collisions)

# A Key is either a str or an int
# An Item contains any piece of data and a Key
class Item:
    def __init__(self, key, item):
        self.key = key      # A Key
        self.item = item    # An item

    def __eq__(self, other):
        return (type(other) == Item
                and self.key == other.key
                and self.item == other.item)

    def __repr__(self):
        return "Item({!r}, {!r})".format(self.key, self.item)

# () -> HashTable
# Returns an empty hash table with an initial size of 8
def empty_hash_table():
    return HashTable()

# HashTable Key Item -> HashTable
# Inserts the Item with the Key into the HashTable
def insert(table, key, item):
    index = hash(key) % table.capacity
    not_inserted = True

    # check for a collision
    if len(table.table[index]) != 0:
        table.collisions += 1

    # check for a duplicate key, and if so then replace its item with the item passed in
    for a in table.table[index]:
        if not_inserted and type(a) == Item and a.key == key:
                a.item = item # duplicate key
                not_inserted = False

    # if we havent already inserted an item then append it to the list at the hash index index
    if not_inserted:
        element = Item(key, item)
        table.table[index].append(element)
        table.size += 1

    # account for load factor and grow and rehash if necessary
    if load_factor(table) > 1.5:
        temp = empty_hash_table()
        temp.table = [[] for y in range(table.capacity * 2)]
        temp.capacity = table.capacity * 2

        for i in range(table.capacity):
            for j in table.table[i]:
                if type(j) == Item:
                    temp = insert(temp, j.key, j.item)

        table.table = temp.table
        table.capacity = temp.capacity
        table.size = temp.size
        table.collisions = temp.collisions

    return table

# HashTable Key -> item
# Returns the item from the hash table associated with the key
def get(table, key):
    index = hash(key) % table.capacity

    for a in table.table[index]:
        if type(a) == Item and a.key == key:
            return a.item

    raise LookupError

# HashTable Key -> HashTable
# Removes the key-value pair from the hash table, and returns the resulting hash table
def remove(table, key):
    index = hash(key) % table.capacity

    for a in table.table[index]:
        if type(a) == Item and a.key == key:
            table.table[index].remove(a)
            table.size -= 1
            return table

    raise LookupError

# HashTable -> int
# Returns an int representing the size of the table
def size(table):
    return table.size

# HashTable -> float
# Returns the load factor of the table
def load_factor(table):
    return float(table.size / table.capacity)

# HashTable -> int
# Returns the number of collisions the table has had total
def collisions(table):
    return table.collisions
