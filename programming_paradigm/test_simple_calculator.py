import unittest
from simple_calculator import SimpleCalculator
class Testsimple_calculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3,2),1)
        self.assertEqual(self.calc.subtract(5,2),3)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3,2),6)
        self.assertEqual(self.calc.multiply(3,3),9)
    def test_division(self):
        self.assertEqual(self.calc.divide(10,2),5)
        self.assertEqual(self.calc.divide(15,3),5)
    def test_division_by_zero(self):
        self.assertEqual(self.calc.divide(2,0),"error, cannot divide by zero")
        self.assertEqual(self.calc.divide(11,0),"error, cannot divide by zero")
        



   


#Write at least one test method for each operation (add, subtract, multiply, divide)