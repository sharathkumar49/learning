"""
LeetCode 2150. Find All Lonely Numbers in the Array

Given an integer array nums, a number is lonely if it appears exactly once, and its neighbors (nums[i]-1 and nums[i]+1) do not appear in the array. Return all lonely numbers in any order.

Example:
Input: nums = [10,6,5,8]
Output: [8,10]

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^6
"""

def findLonely(nums):
    from collections import Counter
    c = Counter(nums)
    res = []
    for x in c:
        if c[x] == 1 and c.get(x-1,0) == 0 and c.get(x+1,0) == 0:
            res.append(x)
    return res

# Example usage:
# print(findLonely([10,6,5,8]))  # Output: [8,10]
