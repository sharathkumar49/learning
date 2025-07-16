"""
LeetCode 2364. Count Number of Bad Pairs

Given nums, return the number of bad pairs.

Example:
Input: nums = [4,1,3,3]
Output: 5

Constraints:
- 1 <= nums.length <= 10^5
"""

def countBadPairs(nums):
    from collections import Counter
    n = len(nums)
    good = 0
    c = Counter()
    for i, num in enumerate(nums):
        good += c[i-num]
        c[i-num] += 1
    total = n*(n-1)//2
    return total - good

# Example usage:
# print(countBadPairs([4,1,3,3]))  # Output: 5
