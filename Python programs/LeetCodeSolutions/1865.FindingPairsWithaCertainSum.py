"""
LeetCode 1865. Finding Pairs With a Certain Sum

Design a class FindSumPairs that supports adding and counting pairs from two integer arrays such that their sum equals a given value.

Example:
Input: FindSumPairs([1,1,2,2,2,3], [1,4,5,2,5,4]), add(1,2), count(7)
Output: 2

Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- 1 <= nums1[i], nums2[i] <= 10^5
- 0 <= index < nums2.length
- -10^9 <= val <= 10^9
"""

from collections import Counter

class FindSumPairs:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.count2 = Counter(nums2)
    def add(self, index, val):
        self.count2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.count2[self.nums2[index]] += 1
    def count(self, tot):
        res = 0
        for a in self.nums1:
            res += self.count2[tot - a]
        return res

# Example usage:
pairs = FindSumPairs([1,1,2,2,2,3], [1,4,5,2,5,4])
pairs.add(1,2)
print(pairs.count(7))  # Output: 2
