import unittest
from poiskMax import large


class TestPoiskMax(unittest.TestCase):
    def test_large(self):
        list = [1, -18, 0, -6, 18]
        res = large(list)
        max = 18
        self.assertEqual(res, max)  # add assertion here


if __name__ == '__main__':
    unittest.main()
