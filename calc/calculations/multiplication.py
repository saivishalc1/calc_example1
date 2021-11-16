"""Multiplication Class"""
from calc.calculations.calculation import Calculation

class Multiplication(Calculation):
    """multiplication calculation object"""
    def get_result(self):
        """get the multiplication results"""
        list_multiply = []
        for value in self.values:
            list_multiply.append(value)
        result = list_multiply[0]
        for num in range(1, len(list_multiply)):
            result = result * list_multiply[num]
        return result
