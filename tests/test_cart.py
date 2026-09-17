import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cart import has_price, is_empty, item_count, total


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


class HasPriceTest(unittest.TestCase):
    def test_cart_with_matching_price(self):
        self.assertTrue(has_price([(2, 3), (5, 1)], 5))

    def test_cart_without_matching_price(self):
        self.assertFalse(has_price([(2, 3), (5, 1)], 4))

    def test_empty_cart_has_no_price(self):
        self.assertFalse(has_price([], 2))


if __name__ == "__main__":
    unittest.main()
