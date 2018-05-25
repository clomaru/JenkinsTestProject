import unittest
import calculator

class Test(unittest.TestCase):

    def testAddFunct(self):

        val1 = 2
        val2 = 3
        expected = 6
        actual = calculator.addFunc(val1, val2)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
