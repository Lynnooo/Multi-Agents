
def sum_list(numbers):
    """
    Calculate the sum of a list of numbers.

    Args:
    numbers (list): A list of numbers (integers or floats).

    Returns:
    float: The sum of the numbers in the list.
    """
    return sum(numbers)

# Test cases
def test_sum_list():
    assert sum_list([1, 2, 3, 4]) == 10, "Test case 1 failed"
    assert sum_list([1.5, 2.5, -1]) == 3.0, "Test case 2 failed"
    assert sum_list([-5, -1, -3, -2]) == -11, "Test case 3 failed"
    assert sum_list([0, 0, 0, 0]) == 0, "Test case 4 failed"
    assert sum_list([1/3, 2/3]) == 1.0, "Test case 5 failed"

# Running test cases
test_sum_list()
