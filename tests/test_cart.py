import unittest
from cart import is_empty, item_count, total


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


class IsEmptyTest(unittest.TestCase):
    def test_empty_cart_is_empty(self):
        self.assertTrue(is_empty([]))

    def test_cart_with_one_item_is_not_empty(self):
        self.assertFalse(is_empty([(2, 3)]))

    def test_cart_with_several_items_is_not_empty(self):
        self.assertFalse(is_empty([(2, 3), (5, 1)]))


if __name__ == "__main__":
    unittest.main()
