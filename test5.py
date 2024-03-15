import unittest
from exercise5 import reverse_ascending

class TestReverseAscending(unittest.TestCase):
    
    def test_reverse_ascending(self):

        # list with odd numbers and zero
        self.assertEqual(reverse_ascending([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        
        # list with negative odd numbers
        self.assertEqual(reverse_ascending(([5, 7, 10, 4, 2, 7, 8, 1, 3])), [10, 7, 5, 4, 8, 7, 2, 3, 1])
        
        # list with odd decimals
        self.assertEqual(reverse_ascending([5, 4, 3, 2, 1]), [5, 4, 3, 2, 1])
        self.assertEqual(reverse_ascending([]), [])

if __name__ == '__main__':
    unittest.main()
