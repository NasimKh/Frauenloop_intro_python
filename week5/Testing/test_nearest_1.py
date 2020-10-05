#test_nearest_1.py


from nearest_num import nearest_square
import unittest


class TestNearest(unittest.TestCase):
    """
    Test class for the nearest function using
    python unit test.
    """


    def test_nearest_square(self):

        self.assertEqual(nearest_square(23) , 16)
        self.assertEqual(nearest_square(9) , 9)
        self.assertEqual(nearest_square(-10) , 0)
        self.assertEqual(nearest_square(0) , 0)

if __name__ == '__main__':
    unittest.main()
