import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_exponentiation(self, ):
        assert self.calc.exponentiation(self, 2, 3)

    def teardown(self):
        print('Выполнение метода Teardown')

