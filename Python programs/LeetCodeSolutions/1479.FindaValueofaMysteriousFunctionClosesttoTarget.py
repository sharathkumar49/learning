"""
LeetCode 1479. Find a Value of a Mysterious Function Closest to Target

Given an integer array arr and an integer target, return the minimum absolute difference between the result of applying bitwise AND to any subarray of arr and target.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i], target <= 10^6

Example:
Input: arr = [9,12,3,7,15], target = 5
Output: 2
"""
def closestToTarget(arr, target):
    res = float('inf')
    s = set()
    for x in arr:
        s = {x & y for y in s} | {x}
        for v in s:
            res = min(res, abs(v - target))
    return res

# Example usage:
arr = [9,12,3,7,15]
target = 5
print(closestToTarget(arr, target))  # Output: 2
