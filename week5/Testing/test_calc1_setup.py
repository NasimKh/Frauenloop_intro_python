

from calc import calculator
import unittest

class TestCalc(unittest.TestCase):
    """
    Test class for the calculator function using
    python unit test.
    """
    def setUp(self):
        self.set1 = calculator(10 , 6)
        self.set2 = calculator(-5 , 5)
        self.set3 = calculator(-6 , -5)
        self.set4 = calculator(-6 , 0)

    def tearDown(self):
        pass

    def test_add(self):
        #cl= calculator(10,5)
        self.assertEqual(calculator.add(self.set1), 16)
        self.assertEqual(calculator.add(self.set2), 0)
        self.assertEqual(calculator.add(self.set3), -11)
        self.assertEqual(calculator.add(self.set4), -6)


    def test_sub(self):
        #cl= calculator(10,5)
        self.assertEqual(calculator.sub(self.set1), 4)
        self.assertEqual(calculator.sub(self.set2), -10)
        self.assertEqual(calculator.sub(self.set3), -1)
        self.assertEqual(calculator.sub(self.set4), -6)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(self.set1), 60)
        self.assertEqual(calculator.multiply(self.set2), -25)
        self.assertEqual(calculator.multiply(self.set3), 30)
        self.assertEqual(calculator.multiply(self.set4), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(self.set1), 1.6666666666666667
)
        self.assertEqual(calculator.divide(self.set2), -1)
        self.assertEqual(calculator.divide(self.set3), 1.2)
        # testing exception
        #self.assertRaises(ValueError , calculator.divide , self.set1)

        # testing exception using context manager
        with self.assertRaises(ValueError) :
            calculator.divide(self.set1)


if __name__ == '__main__':
    unittest.main()
