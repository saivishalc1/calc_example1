"""Testing Division"""
import pytest
from calc.calculations.division import Division

def test_calculation_subtraction():
    """testing that our calculator has a static method for multiplication"""
    nums = (8.0, 2.0)
    division = Division(nums)
    assert division.get_result() == 4.0

def Value_error_test():
    """This shows when not using a number for division"""
    nums = ("1.0", "1.0")
    error1_test = Division(nums)
    with pytest.raises(ValueError) as error1:
        error1_test.get_result()
    assert error1.type == ValueError

def Zero_division_error_test():
    """This shows when divided by 0 there will be an error that happens"""
    nums = (1.0, 0.0)
    error1_test = Division(nums)
    with pytest.raises(ZeroDivisionError) as error2:
        error1_test.get_result()
    assert error2.type == ZeroDivisionError


