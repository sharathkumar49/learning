"""
LeetCode 1994. The Number of Good Subsets

Given an array nums, return the number of good subsets. A good subset is a subset where the product of its elements is a product of one or more distinct primes.

Example:
Input: nums = [1,2,3,4]
Output: 6

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 30
"""

MOD = 10**9+7

def numberOfGoodSubsets(nums):
    from collections import Counter
    primes = [2,3,5,7,11,13,17,19,23,29]
    masks = [0] + [1<<i for i in range(10)]
    cnt = Counter(nums)
    dp = [0]*1024
    dp[0] = 1
    for x in range(2, 31):
        if cnt[x]:
            mask = 0
            y = x
            for i, p in enumerate(primes):
                c = 0
                while y % p == 0:
                    y //= p
                    c += 1
                if c > 1:
                    mask = -1
                    break
                if c == 1:
                    mask |= 1<<i
            if y > 1 or mask == -1:
                continue
            for state in range(1023, -1, -1):
                if state & mask == 0:
                    dp[state|mask] = (dp[state|mask] + dp[state]*cnt[x]) % MOD
    res = sum(dp[1:]) % MOD
    for _ in range(cnt[1]):
        res = res * 2 % MOD
    return res

# Example usage:
# print(numberOfGoodSubsets([1,2,3,4]))  # Output: 6
