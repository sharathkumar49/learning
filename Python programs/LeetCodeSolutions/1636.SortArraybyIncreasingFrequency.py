"""
LeetCode 1636. Sort Array by Increasing Frequency

Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Example 1:
Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]

Constraints:
- 1 <= nums.length <= 100
- -100 <= nums[i] <= 100
"""

def frequencySort(nums):
    from collections import Counter
    c = Counter(nums)
    return sorted(nums, key=lambda x: (c[x], -x))

# Example usage:
# nums = [1,1,2,2,2,3]
# print(frequencySort(nums))  # Output: [3,1,1,2,2,2]
