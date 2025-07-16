"""
LeetCode 2342. Max Sum of Pair With Equal Sum of Digits

Given nums, return the maximum sum of a pair with equal sum of digits.

Example:
Input: nums = [51,71,17,42]
Output: 93

Constraints:
- 1 <= nums.length <= 10^4
- 1 <= nums[i] <= 10^9
"""

def maximumSum(nums):
    from collections import defaultdict
    d = defaultdict(list)
    for num in nums:
        s = sum(int(x) for x in str(num))
        d[s].append(num)
    res = -1
    for v in d.values():
        if len(v) >= 2:
            v.sort(reverse=True)
            res = max(res, v[0]+v[1])
    return res

# Example usage:
# print(maximumSum([51,71,17,42]))  # Output: 93
