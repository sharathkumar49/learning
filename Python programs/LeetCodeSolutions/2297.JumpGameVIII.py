"""
LeetCode 2297. Jump Game VIII

Given nums, return true if you can reach the last index.

Example:
Input: nums = [2,3,1,1,4]
Output: True

Constraints:
- 1 <= nums.length <= 10^5
"""

def canJump(nums):
    max_reach = 0
    for i, num in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i+num)
    return True

# Example usage:
# print(canJump([2,3,1,1,4]))  # Output: True
