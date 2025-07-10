"""
LeetCode 2190. Most Frequent Number Following Key In an Array

Given an array nums and an integer key, return the most frequent number that immediately follows key in nums. If there is a tie, return the smallest such number.

Example:
Input: nums = [1,100,200,1,100], key = 1
Output: 100

Constraints:
- 2 <= nums.length <= 1000
- 1 <= key <= 1000
"""

def mostFrequent(nums, key):
    from collections import Counter
    c = Counter()
    for i in range(len(nums)-1):
        if nums[i] == key:
            c[nums[i+1]] += 1
    return min([k for k,v in c.items() if v == max(c.values())])

# Example usage:
# print(mostFrequent([1,100,200,1,100], 1))  # Output: 100
