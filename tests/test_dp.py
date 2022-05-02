import unittest
from examples.dp import logic_A


class Test_DP(unittest.TestCase):
    def test_A(self):
        result = logic_A(4, [10, 30, 40, 20])
        self.assertEqual(30, result)


if __name__ == "__main__":
    unittest.main()
