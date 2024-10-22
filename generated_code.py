
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    sorted_arr = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_arr.append(left[left_index])
            left_index += 1
        else:
            sorted_arr.append(right[right_index])
            right_index += 1

    sorted_arr.extend(left[left_index:])
    sorted_arr.extend(right[right_index:])

    return sorted_arr

# Test case 1
test_case_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
assert merge_sort(test_case_1) == sorted(test_case_1), "Test case 1 failed"

# Test case 2
test_case_2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
assert merge_sort(test_case_2) == sorted(test_case_2), "Test case 2 failed"

# Test case 3
test_case_3 = [1]
assert merge_sort(test_case_3) == [1], "Test case 3 failed"

# Test case 4
test_case_4 = []
assert merge_sort(test_case_4) == [], "Test case 4 failed"

# Test case 5
test_case_5 = [2, 3, 5, 1, 4]
assert merge_sort(test_case_5) == [1, 2, 3, 4, 5], "Test case 5 failed"

print("All test cases passed!")
