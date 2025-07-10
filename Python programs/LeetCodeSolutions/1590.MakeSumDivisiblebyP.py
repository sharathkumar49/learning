"""
LeetCode 1590. Make Sum Divisible by P

Given an array of positive integers nums and an integer p, remove the smallest subarray such that the sum of the remaining elements is divisible by p. Return the length of the smallest subarray, or -1 if impossible.

Example 1:
Input: nums = [3,1,4,2], p = 6
Output: 1

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= p <= 10^9
"""

def minSubarray(nums, p):
    total = sum(nums)
    r = total % p
    if r == 0:
        return 0
    prefix = {0: -1}
    cur = 0
    res = len(nums)
    for i, x in enumerate(nums):
        cur = (cur + x) % p
        prefix[cur] = i
        want = (cur - r) % p
        if want in prefix:
            res = min(res, i - prefix[want])
    return res if res < len(nums) else -1

# Example usage:
# nums = [3,1,4,2]
# p = 6
# print(minSubarray(nums, p))  # Output: 1
