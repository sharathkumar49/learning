"""
LeetCode 1679. Max Number of K-Sum Pairs

Given an array nums and an integer k, return the maximum number of operations to remove pairs that sum to k.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= 10^9
"""

def maxOperations(nums, k):
    from collections import Counter
    c = Counter(nums)
    res = 0
    for x in c:
        y = k - x
        if y in c:
            if x == y:
                res += c[x] // 2
            elif x < y:
                res += min(c[x], c[y])
    return res

# Example usage:
# nums = [1,2,3,4]
# k = 5
# print(maxOperations(nums, k))  # Output: 2
