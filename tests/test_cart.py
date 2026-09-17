import unittest
from cart import item_count, total


class TotalTest(unittest.TestCase):
    def test_quantity_counts(self):
        self.assertEqual(total([(2, 3), (5, 1)]), 11)


class ItemCountTest(unittest.TestCase):
    def test_empty_cart(self):
        self.assertEqual(item_count([]), 0)

    def test_single_item_multiple_quantity(self):
        self.assertEqual(item_count([(2, 3)]), 3)

    def test_several_items(self):
        self.assertEqual(item_count([(2, 3), (5, 1), (4, 2)]), 6)


if __name__ == "__main__":
    unittest.main()
