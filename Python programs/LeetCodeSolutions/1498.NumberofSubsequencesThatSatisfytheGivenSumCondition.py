"""
LeetCode 1498. Number of Subsequences That Satisfy the Given Sum Condition

Given an array of integers nums and an integer target, return the number of non-empty subsequences such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 10^9 + 7.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
- 1 <= target <= 10^6

Example:
Input: nums = [3,5,6,7], target = 9
Output: 4
"""
def numSubseq(nums, target):
    nums.sort()
    mod = 10**9 + 7
    res = 0
    l, r = 0, len(nums) - 1
    pow2 = [1] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        pow2[i] = pow2[i-1] * 2 % mod
    while l <= r:
        if nums[l] + nums[r] <= target:
            res = (res + pow2[r-l]) % mod
            l += 1
        else:
            r -= 1
    return res

# Example usage:
nums = [3,5,6,7]
target = 9
print(numSubseq(nums, target))  # Output: 4
