import unittest
from exercise2 import index_power
    
class TestIndexPower(unittest.TestCase):
    def test_valid_index(self):
        self.assertEqual(index_power([1, 2, 3, 4], 2), 9)
        self.assertEqual(index_power([0, 1, 2, 3], 0), 1)
        self.assertEqual(index_power([-1, -2, -3, -4], 3), -64)

if __name__ == '__main__':
    unittest.main()