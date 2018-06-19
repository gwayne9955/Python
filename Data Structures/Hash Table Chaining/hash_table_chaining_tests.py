import unittest
from hash_table_chaining import *

class TestList(unittest.TestCase):

    def test_empty_hash_table(self):
        self.assertEqual(empty_hash_table(), HashTable())

    def test_repr(self):
        self.assertEqual(repr(empty_hash_table()), "HashTable([[], [], [], [], [], [], [], []], 8, 0, 0)")

    def test_item_eq(self):
        a = Item(123, "l")
        b = Item(123, "l")
        self.assertEqual(a, b)
        c = Item(123, "ll")
        self.assertEqual(a == c, False)

    def test_insert(self):
        # self.assertEqual(insert(None))
        h = empty_hash_table()
        answer = empty_hash_table()
        answer.table[1].append(Item(89,"lol"))
        answer.size += 1
        self.assertEqual(insert(h, 89, "lol"), answer)
        answer.table[1].append(Item(97, "second"))
        answer.size += 1
        answer.collisions += 1
        self.assertEqual(insert(h, 97, "second"), answer)
        answer.table[1][0] = Item(89, "duplicate")
        answer.collisions += 1
        self.assertEqual(insert(h, 89, "duplicate"), answer)
        answer.table[1].append(Item(81, "third"))
        answer.size += 1
        answer.collisions = 3
        self.assertEqual(insert(h, 81, "third"), answer)

        insert(h, 0, "one")
        insert(h, 1, 2)
        insert(h, 2, 3)
        insert(h, 3, 4)
        insert(h, 4, 5)
        insert(h, 5, 6)
        insert(h, 6, 7)
        insert(h, 7, 8)
        insert(h, 8, "nice")
        insert(h, 9, "here we go")
        self.assertEqual(repr(h), "HashTable([[Item(0, 'one')], [Item(97, 'second'), Item(81, 'third'), Item(1, 2)], [Item(2, 3)], [Item(3, 4)], [Item(4, 5)], [Item(5, 6)], [Item(6, 7)], [Item(7, 8)], [Item(8, 'nice')], [Item(89, 'duplicate'), Item(9, 'here we go')], [], [], [], [], [], []], 16, 13, 3)")

    def test_get(self):
        h = empty_hash_table()
        self.assertRaises(LookupError, get, h, 9)
        insert(h, 123, "key")
        self.assertEqual(get(h, 123), "key")
        self.assertRaises(LookupError, get, h, 9)

    def test_remove(self):
        h = empty_hash_table()
        self.assertRaises(LookupError, remove, h, 9)
        insert(h, 123, "key")
        answer = empty_hash_table()
        self.assertEqual(remove(h, 123), answer)
        insert(h, 12, "keyy")
        insert(h, 13, "keyyy")
        insert(answer, 13, "keyyy")
        self.assertEqual(remove(h, 12), answer)

    def test_size(self):
        h = empty_hash_table()
        self.assertEqual(size(h), 0)
        insert(h, 0, "one")
        insert(h, 1, 2)
        insert(h, 2, 3)
        insert(h, 3, 4)
        insert(h, 4, 5)
        insert(h, 5, 6)
        insert(h, 6, 7)
        insert(h, 7, 8)
        insert(h, 8, "nice")
        insert(h, 9, "here we go")
        self.assertEqual(size(h), 10)

    def test_load_factor(self):
        h = empty_hash_table()
        self.assertEqual(load_factor(h), 0.0)
        insert(h, 0, "one")
        insert(h, 1, 2)
        insert(h, 2, 3)
        insert(h, 3, 4)
        insert(h, 4, 5)
        insert(h, 5, 6)
        insert(h, 6, 7)
        insert(h, 7, 8)
        insert(h, 8, "nice")
        insert(h, 9, "here we go")
        self.assertEqual(load_factor(h), 1.25)
        insert(h, 10, "one")
        insert(h, 11, 2)
        insert(h, 12, 3)
        insert(h, 13, 4)
        insert(h, 14, 5)
        insert(h, 15, 6)
        insert(h, 16, 7)
        insert(h, 17, 8)
        insert(h, 18, "nice")
        insert(h, 19, "here we go")
        self.assertEqual(load_factor(h), 1.25)

    def test_collisions(self):
        h = empty_hash_table()
        self.assertEqual(load_factor(h), 0.0)
        insert(h, 0, "one")
        insert(h, 1, 2)
        insert(h, 2, 3)
        insert(h, 3, 4)
        insert(h, 4, 5)
        insert(h, 5, 6)
        insert(h, 6, 7)
        insert(h, 7, 8)
        insert(h, 8, "nice")
        insert(h, 9, "here we go")
        self.assertEqual(load_factor(h), 1.25)
        insert(h, 10, "one")
        insert(h, 11, 2)
        insert(h, 12, 3)
        insert(h, 13, 4)
        insert(h, 14, 5)
        insert(h, 15, 6)
        insert(h, 16, 7)
        insert(h, 17, 8)
        insert(h, 18, "nice")
        insert(h, 19, "here we go")
        self.assertEqual(load_factor(h), 1.25)
        self.assertEqual(collisions(h), 4)



if __name__ == '__main__':
    unittest.main()