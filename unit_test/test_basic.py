import unittest


class TestMyCode(unittest.TestCase):

    def setUp(self) -> None:
        print("Starting testing ...")

    def test_is_a_gregater_than_b(self):
        a = 7
        b = 6
        self.assertTrue(a > b, "A is not greater than B")

    def test_x_is_equal_to_y(self):
        x = 7
        y = 7
        self.assertTrue(x == y, "X is not equal Y")

    def tearDown(self) -> None:
        print("Clear data. Testing is done")

if __name__ == '__main__':
    unittest.main()

# run from command line
# python -m unittest -v
