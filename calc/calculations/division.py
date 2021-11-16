"""Division Class - with exceptions for 3 errors"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """division calculation object"""
    def get_result(self):
        """get the division results"""
        list_div = []
        for value in self.values:
            list_div.append(value)
        result = list_div[0]
        for num in range(1, len(list_div)):
            try:
                result /= list_div[num]
            except ValueError as error1:
                raise ValueError from error1
            except ZeroDivisionError as error2:
                raise ZeroDivisionError from error2
            except IndexError as error3:
                raise IndexError from error3
            else:
                continue
        return result
