"""
LeetCode 2453. Destroy Sequential Targets

Given an array and space, return the minimum number of moves to destroy all targets.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= space <= 10^9
"""

def destroyTargets(nums, space):
    from collections import Counter
    cnt = Counter(x%space for x in nums)
    max_cnt = max(cnt.values())
    return min(x for x in nums if cnt[x%space]==max_cnt)

# Example usage:
# print(destroyTargets([3,7,2,9,1], 3))  # Output: 3
