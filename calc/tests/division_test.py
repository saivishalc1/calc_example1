"""Testing Division"""
from calc.calculations.division import Division


def test_calculation_subtraction():
    """testing that our calculator has a static method for multiplication"""
    # Arrange
    nums = (8.0, 2.0)
    division = Division(nums)
    # Act
    # Assert
    assert division.get_result() == 4.0

def zerodivisionerror_test():
    """This shows when divided by 0 there will be an error that happens"""
    nums = (12.0,0.0)
    era_test = Division(nums)


