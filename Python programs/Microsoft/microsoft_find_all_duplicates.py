# Microsoft: Find All Duplicates in an Array
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others once.
# Find all elements that appear twice.

def find_duplicates(nums):
    res = []
    for n in nums:
        idx = abs(n) - 1
        if nums[idx] < 0:
            res.append(abs(n))
        else:
            nums[idx] = -nums[idx]
    return res

if __name__ == "__main__":
    arr1 = [4,3,2,7,8,2,3,1]
    print(find_duplicates(arr1))  # Output: [2,3]
    arr2 = [1,1,2]
    print(find_duplicates(arr2))  # Output: [1]
    arr3 = [1]
    print(find_duplicates(arr3))  # Output: []
