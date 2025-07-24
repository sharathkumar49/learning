"""
LeetCode 2598. Smallest Missing Non-negative Integer After Operations

Given nums and value, return the smallest missing non-negative integer after operations.

Constraints:
- 1 <= nums.length <= 10^5
"""

def findSmallestInteger(nums, value):
    from collections import Counter
    count = Counter([x % value for x in nums])
    i = 0
    while True:
        if count[i % value]:
            count[i % value] -= 1
            i += 1
        else:
            return i
# Example usage:
# print(findSmallestInteger([1,2,3,4,0,2,2,1,1], 2))  # Output: 5
