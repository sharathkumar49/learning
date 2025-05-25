# Amazon: Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
    return []

if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    print(two_sum(arr, 9))  # Output: [0, 1]
    arr2 = [3, 2, 4]
    print(two_sum(arr2, 6))  # Output: [1, 2]
