"""Testing Addition"""
from calc.calculations.addition import Addition


def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    # Arrange
    nums = (3.0, 2.0)
    addition = Addition(nums)
    # Act
    # Assert
    assert addition.get_result() == 5.0
