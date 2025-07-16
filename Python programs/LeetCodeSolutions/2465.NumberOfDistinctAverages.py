"""
LeetCode 2465. Number of Distinct Averages

Given an array, return the number of distinct averages.

Constraints:
- 2 <= nums.length <= 100
"""

def distinctAverages(nums):
    nums.sort()
    s = set()
    while nums:
        s.add((nums[0]+nums[-1])/2)
        nums.pop(0)
        nums.pop()
    return len(s)

# Example usage:
# print(distinctAverages([4,1,4,0,3,5]))  # Output: 2
