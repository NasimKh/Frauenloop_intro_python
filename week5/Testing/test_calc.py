from calc import calculator
import unittest


class TestCalc(unittest.TestCase):
    """
    Test class for the calculator function using
    python unit test.
    """


    def test_add(self):
        cl= calculator(10,5)
        self.assertEqual(calculator.add(cl), 15)
        self.assertEqual(calculator.add(calculator(-5,5)), 0)
        self.assertEqual(calculator.add(calculator(-6,-5)), -11)


#if __name__ == '__main__':
    #unittest.main()
