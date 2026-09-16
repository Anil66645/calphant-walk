import unittest
from cart import total


class TotalTest(unittest.TestCase):
    def test_quantity_counts(self):
        self.assertEqual(total([(2, 3), (5, 1)]), 11)


if __name__ == "__main__":
    unittest.main()
