
def sum_list(lst):
    """Calculate the sum of a list of numbers."""
    return sum(lst)

# Test case 1
def test_sum_list_case1():
    input_list = [1, 2, 3, 4, 5]
    expected_output = 15
    actual_output = sum_list(input_list)
    assert actual_output == expected_output, f"Expected {expected_output}, but got {actual_output}"

# Test case 2
def test_sum_list_case2():
    input_list = [-1, 0, 1, 2]
    expected_output = 2
    actual_output = sum_list(input_list)
    assert actual_output == expected_output, f"Expected {expected_output}, but got {actual_output}"

# Running test cases
if __name__ == "__main__":
    test_sum_list_case1()
    test_sum_list_case2()
    print("All test cases passed!")
