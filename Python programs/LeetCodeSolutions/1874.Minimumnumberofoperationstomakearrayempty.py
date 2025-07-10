"""
LeetCode 1874. Minimum Number of Operations to Make the Array Empty

You are given an integer array nums. In one operation, you can remove two equal elements or three equal elements from the array. Return the minimum number of operations to make the array empty, or -1 if it is impossible.

Example:
Input: nums = [2,3,3,2,2,4,2,3,4]
Output: 4

Constraints:
- 2 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
"""

from collections import Counter

def minOperations(nums):
    cnt = Counter(nums)
    res = 0
    for v in cnt.values():
        if v == 1:
            return -1
        res += (v + 2) // 3
    return res

# Example usage:
# print(minOperations([2,3,3,2,2,4,2,3,4]))  # Output: 4
