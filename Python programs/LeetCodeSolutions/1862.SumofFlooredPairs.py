"""
LeetCode 1862. Sum of Floored Pairs

Given an integer array nums, return the sum of floor(nums[i] / nums[j]) for all pairs (i, j). Since the answer may be large, return it modulo 10^9 + 7.

Example:
Input: nums = [2,5,9]
Output: 10

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

MOD = 10**9 + 7

def sumOfFlooredPairs(nums):
    max_num = max(nums)
    count = [0] * (max_num + 2)
    for num in nums:
        count[num] += 1
    prefix = [0] * (max_num + 2)
    for i in range(1, max_num + 2):
        prefix[i] = prefix[i-1] + count[i]
    res = 0
    for x in range(1, max_num + 1):
        if count[x]:
            for k in range(1, (max_num // x) + 1):
                res += count[x] * (prefix[min((k+1)*x-1, max_num)] - prefix[k*x-1]) * k
                res %= MOD
    return res

# Example usage:
print(sumOfFlooredPairs([2,5,9]))  # Output: 10
