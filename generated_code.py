
def sum_list(lst):
    return sum(lst)

# Test Case 1
def test_sum_list():
    test_list = [1, 2, 3, 4]
    expected_sum = 10
    assert sum_list(test_list) == expected_sum, f"Expected sum of {test_list} to be {expected_sum}, but got {sum_list(test_list)}"

# Test Case 2
def test_sum_list_negative_numbers():
    test_list = [-1, -2, -3, -4]
    expected_sum = -10
    assert sum_list(test_list) == expected_sum, f"Expected sum of {test_list} to be {expected_sum}, but got {sum_list(test_list)}"

# Running test cases
test_sum_list()
test_sum_list_negative_numbers()
