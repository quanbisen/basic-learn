import unittest
from src.calculator import add, subtract


class CalculatorTestCase(unittest.TestCase):

    def test_add(self):
        result = add(1, 2)
        self.assertEqual(result, 3)

    def test_subtract(self):
        result = subtract(2, 1)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()


