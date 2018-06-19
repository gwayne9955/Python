import unittest
from postfix import *

class TestPostfix(unittest.TestCase):

    def test_postfix(self):
        self.assertAlmostEqual(postfix_calc("1 2 + 4 *"), 12.0)
        self.assertAlmostEqual(postfix_calc("1.000 2 + 4 * 7 / 3 - 8 +"), 6.714285714285714)
        self.assertAlmostEqual(postfix_calc("4.0"), 4.0)
        self.assertAlmostEqual(postfix_calc("4.0 4.5 + 8.1 0.3 + + 1 +"), 17.9)

    def test00_interface(self):
        postfix_calc("1 1 +")

if __name__ == "__main__":
    unittest.main()
