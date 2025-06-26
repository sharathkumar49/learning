# Microsoft: Find Missing Number
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

if __name__ == "__main__":
    arr1 = [3,0,1]
    print(missing_number(arr1))  # Output: 2
    arr2 = [0,1]
    print(missing_number(arr2))  # Output: 2
    arr3 = [9,6,4,2,3,5,7,0,1]
    print(missing_number(arr3))  # Output: 8
