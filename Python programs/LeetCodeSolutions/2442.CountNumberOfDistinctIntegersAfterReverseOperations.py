"""
LeetCode 2442. Count Number of Distinct Integers After Reverse Operations

Given an array, count the number of distinct integers after reverse operations.

Constraints:
- 1 <= nums.length <= 10^5
"""

def countDistinctIntegers(nums):
    s = set(nums)
    for x in nums:
        s.add(int(str(x)[::-1]))
    return len(s)

# Example usage:
# print(countDistinctIntegers([1,13,10,12,31]))  # Output: 6
