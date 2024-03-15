import unittest
from exercise4 import chunking_by


class TestChunkingBy(unittest.TestCase):
    def test_chunking(self):
        self.assertEqual(chunking_by([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]])
        self.assertEqual(chunking_by([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
        self.assertEqual(chunking_by([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15), [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
        self.assertEqual(chunking_by([], 5), [])


if __name__ == '__main__':
    unittest.main()