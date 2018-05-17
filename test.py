import unittest
import main

class Test(unittest.TestCase):

    def testAddFunct(self):

        val1 = 2
        val2 = 3
        expected = 5
        actual = main.addFunc(val1, val2)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
