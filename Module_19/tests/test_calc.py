import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_exponentiation(self):
        assert self.calc.exponentiation(self, 3, 2) == 9

    def test_multiply(self):
        assert self.calc.multiply(self, 3, 2) == 6

    def test_division(self):
        assert self.calc.division(self, 6, 2) == 3

    def test_subtraction(self):
        assert self.calc.subtraction(self, 3, 2) == 1

    def test_adding(self):
        assert self.calc.adding(self, 2, 3) == 5

    def teardown(self):
        print('Выполнение метода Teardown')

