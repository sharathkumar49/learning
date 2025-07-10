"""
LeetCode 2172. Maximum AND Sum of Array

Given an integer array nums and an integer numSlots, assign each number to a slot (each slot can hold up to 2 numbers) to maximize the sum of AND of the number and the slot number. Return the maximum sum.

Example:
Input: nums = [1,2,3,4,5,6], numSlots = 3
Output: 9

Constraints:
- 1 <= numSlots <= 9
- 1 <= nums.length <= 2 * numSlots
- 1 <= nums[i] <= 15
"""

def maximumANDSum(nums, numSlots):
    from functools import lru_cache
    n = len(nums)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        res = 0
        for slot in range(numSlots):
            cnt = (mask >> (slot*2)) & 3
            if cnt < 2:
                res = max(res, ((nums[i] & (slot+1)) + dp(i+1, mask + (1<<(slot*2)))) )
        return res
    return dp(0, 0)

# Example usage:
# print(maximumANDSum([1,2,3,4,5,6], 3))  # Output: 9
