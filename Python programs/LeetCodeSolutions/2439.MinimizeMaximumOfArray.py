"""
LeetCode 2439. Minimize Maximum of Array

Given an array, return the minimized maximum value after allowed operations.

Constraints:
- 1 <= nums.length <= 10^5
"""

def minimizeArrayValue(nums):
    res = curr_sum = 0
    for i, num in enumerate(nums):
        curr_sum += num
        res = max(res, (curr_sum+i)//(i+1))
    return res

# Example usage:
# print(minimizeArrayValue([3,7,1,6]))  # Output: 5
