"""
LeetCode 1502. Can Make Arithmetic Progression From Sequence

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression.

Constraints:
- 2 <= arr.length <= 1000
- -10^6 <= arr[i] <= 10^6

Example:
Input: arr = [3,5,1]
Output: True
"""
def canMakeArithmeticProgression(arr):
    arr.sort()
    diff = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] != diff:
            return False
    return True

# Example usage:
arr = [3,5,1]
print(canMakeArithmeticProgression(arr))  # Output: True
