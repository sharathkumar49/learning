"""
LeetCode 1998. GCD Sort of an Array

Given an array nums, return true if it can be sorted by only swapping elements with a common factor greater than 1.

Example:
Input: nums = [7,21,3]
Output: true

Constraints:
- 1 <= nums.length <= 10^5
- 2 <= nums[i] <= 10^5
"""

def gcdSort(nums):
    import math
    n = len(nums)
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        parent[find(x)] = find(y)
    for x in nums:
        for f in range(2, int(x**0.5)+1):
            if x % f == 0:
                union(x, f)
                union(x, x//f)
    for x in nums:
        union(x, x)
    return sorted(nums) == sorted(nums, key=lambda x: find(x))

# Example usage:
# print(gcdSort([7,21,3]))  # Output: True
