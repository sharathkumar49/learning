"""
LeetCode 1300. Sum of Mutated Array Closest to Target

Given an array arr and an integer target, mutate the array by replacing all elements greater than a value with that value. Return the value such that the sum is closest to target.

Constraints:
- 1 <= arr.length <= 10^4
- 1 <= arr[i], target <= 10^5

Example:
Input: arr = [2,3,5], target = 10
Output: 5
"""
def findBestValue(arr, target):
    left, right = 0, max(arr)
    res, diff = 0, float('inf')
    while left <= right:
        mid = (left + right) // 2
        s = sum(min(x, mid) for x in arr)
        if abs(s - target) < diff or (abs(s - target) == diff and mid < res):
            res, diff = mid, abs(s - target)
        if s < target:
            left = mid + 1
        else:
            right = mid - 1
    return res

# Example usage:
arr = [2,3,5]
target = 10
print(findBestValue(arr, target))  # Output: 5
