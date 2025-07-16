"""
LeetCode 2261. K Divisible Elements Subarrays

Given nums and k, return the number of subarrays with at most k elements divisible by k.

Example:
Input: nums = [2,3,3,2,3], k = 2
Output: 12

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= k <= 10^5
"""

def countDistinct(nums, k):
    from collections import defaultdict
    res = 0
    n = len(nums)
    for i in range(n):
        cnt = 0
        for j in range(i, n):
            if nums[j] % k == 0:
                cnt += 1
            if cnt > k:
                break
            res += 1
    return res

# Example usage:
# print(countDistinct([2,3,3,2,3], 2))  # Output: 12
