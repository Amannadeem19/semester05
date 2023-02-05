import unittest
from mycalculator.calculator import CalApp


class TestSimpleCalc(unittest.TestCase):
    def test_add(self):
        self.cal = CalApp(4, 5)
        self.assertEqual(9, self.cal.add())  # add assertion here

    def test_sub(self):
        self.cal = CalApp(6, 4)
        self.assertEqual(2, self.cal.sub())

    def test_div(self):
        self.cal = CalApp(4, 2)
        self.assertEqual(2, self.cal.div())

    def test_mult(self):
        self.cal = CalApp(10, 2)
        self.assertEqual(10, self.cal.mult())


if __name__ == '__main__':
    unittest.main()
