
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Test case 1
test_case_1 = [3, 6, 8, 10, 1, 2, 1]
assert quick_sort(test_case_1) == sorted(test_case_1), "Test case 1 failed"

# Test case 2
test_case_2 = [12, 8, 1, 20, 11, 3, 5, 9, 10]
assert quick_sort(test_case_2) == sorted(test_case_2), "Test case 2 failed"

print("All test cases passed!")
