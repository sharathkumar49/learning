"""
LeetCode 2394. Find Subarrays With Equal Sum

Given an array, return True if there are subarrays of length 2 with equal sum.

Constraints:
- 2 <= nums.length <= 100
"""

def findSubarrays(nums):
    seen = set()
    for i in range(len(nums)-1):
        s = nums[i]+nums[i+1]
        if s in seen:
            return True
        seen.add(s)
    return False

# Example usage:
# print(findSubarrays([4,2,4]))  # Output: True
