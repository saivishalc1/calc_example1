"""division Class"""
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """division calculation object"""
    def get_result(self):
        """get the division results"""
        division_list = []
        for value in self.values:
            division_list.append(value)
        result = division_list[0]
        for num in range(1, len(list)):
            result /= division_list[num]
        return result
