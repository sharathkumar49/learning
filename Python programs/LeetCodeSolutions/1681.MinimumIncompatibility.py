"""
LeetCode 1681. Minimum Incompatibility

Given an array nums and an integer k, partition nums into k subsets of equal size such that the sum of incompatibilities is minimized. Return -1 if impossible.

Example 1:
Input: nums = [1,2,1,4], k = 2
Output: 4

Constraints:
- 1 <= k <= nums.length <= 16
- 1 <= nums[i] <= nums.length
"""

def minimumIncompatibility(nums, k):
    from collections import Counter
    from functools import lru_cache
    n = len(nums)
    if n % k:
        return -1
    size = n // k
    if any(v > k for v in Counter(nums).values()):
        return -1
    @lru_cache(None)
    def dfs(mask):
        if mask == 0:
            return 0
        res = float('inf')
        bits = [i for i in range(n) if mask & (1<<i)]
        if len(bits) < size:
            return res
        for comb in combinations(bits, size):
            vals = [nums[i] for i in comb]
            if len(set(vals)) < size:
                continue
            new_mask = mask
            for i in comb:
                new_mask ^= (1<<i)
            res = min(res, max(vals)-min(vals) + dfs(new_mask))
        return res
    from itertools import combinations
    ans = dfs((1<<n)-1)
    return ans if ans < float('inf') else -1

# Example usage:
# nums = [1,2,1,4]
# k = 2
# print(minimumIncompatibility(nums, k))  # Output: 4
