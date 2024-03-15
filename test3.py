import unittest
from exercise3 import remove_all_after

class TestRemoveAllAfter(unittest.TestCase):
    def test_removing_elements(self):
        self.assertEqual(remove_all_after([1, 2, 3, 4, 5], 3), [1, 2, 3])
        self.assertEqual(remove_all_after([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])
        self.assertEqual(remove_all_after([1, 2, 3, 4, 5], 6), [1, 2, 3, 4, 5])
        self.assertEqual(remove_all_after([], 1), [])
        self.assertEqual(remove_all_after([1], 1), [1])


if __name__ == '__main__':
    unittest.main()