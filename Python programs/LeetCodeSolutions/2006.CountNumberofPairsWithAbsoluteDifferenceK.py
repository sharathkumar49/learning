"""
LeetCode 2006. Count Number of Pairs With Absolute Difference K

Given an integer array nums and an integer k, return the number of pairs (i, j) with i < j such that |nums[i] - nums[j]| == k.

Example:
Input: nums = [1,2,2,1], k = 1
Output: 4

Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100
- 1 <= k <= 99
"""

def countKDifference(nums, k):
    from collections import Counter
    count = Counter(nums)
    return sum(count[x] * count[x + k] for x in count)

# Example usage:
# print(countKDifference([1,2,2,1], 1))  # Output: 4
