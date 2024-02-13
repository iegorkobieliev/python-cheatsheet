import unittest


def add(x, y):
    return x + y


class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_positive_numbers_negative(self):
        self.assertEqual(add(2, 2), 5)


if __name__ == '__main__':
    unittest.main()
