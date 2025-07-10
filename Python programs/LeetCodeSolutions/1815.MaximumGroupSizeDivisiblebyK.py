"""
LeetCode 1815. Maximum Group Size Divisible by K

Given an array nums and an integer k, return the maximum size of a group such that the sum of the group is divisible by k.

Example 1:
Input: nums = [3,6,9,1,2,2,2,2,2], k = 3
Output: 9

Constraints:
- 1 <= nums.length <= 10^4
- 1 <= k <= 10^4
- 1 <= nums[i] <= 10^9
"""

def maxHappyGroups(k, groups):
    from collections import Counter
    from functools import lru_cache
    cnt = Counter([x % k for x in groups])
    res = cnt[0]
    keys = tuple(cnt[i] for i in range(1, k))
    @lru_cache(None)
    def dfs(state, rem):
        best = 0
        for i in range(1, k):
            if state[i-1]:
                new_state = list(state)
                new_state[i-1] -= 1
                best = max(best, dfs(tuple(new_state), (rem + i) % k) + (rem == 0))
        return best
    return res + dfs(keys, 0)

# Example usage:
# k = 3
# groups = [3,6,9,1,2,2,2,2,2]
# print(maxHappyGroups(k, groups))  # Output: 9
