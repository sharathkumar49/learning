"""
LeetCode 2263. Make Array Non-Decreasing or Non-Increasing

Given nums, return the minimum number of moves to make the array non-decreasing or non-increasing.

Example:
Input: nums = [3,2,1,4]
Output: 1

Constraints:
- 1 <= nums.length <= 10^5
"""

def minMoves(nums):
    inc = dec = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            inc += 1
        if nums[i] > nums[i-1]:
            dec += 1
    return min(inc, dec)

# Example usage:
# print(minMoves([3,2,1,4]))  # Output: 1
