"""
LeetCode 1460. Make Two Arrays Equal by Reversing Subarrays

Given two integer arrays of equal length target and arr, return true if it is possible to make arr equal to target by reversing any number of subarrays (possibly zero or more).

Constraints:
- 1 <= target.length == arr.length <= 1000
- 1 <= target[i], arr[i] <= 1000

Example:
Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
"""
def canBeEqual(target, arr):
    return sorted(target) == sorted(arr)

# Example usage:
target = [1,2,3,4]
arr = [2,4,1,3]
print(canBeEqual(target, arr))  # Output: True
