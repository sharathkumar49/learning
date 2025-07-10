"""
LeetCode 1995. Count Special Quadruplets

Given an array nums, return the number of quadruplets (a, b, c, d) such that nums[a] + nums[b] + nums[c] == nums[d] and a < b < c < d.

Example:
Input: nums = [1,2,3,6]
Output: 1

Constraints:
- 4 <= nums.length <= 50
- 1 <= nums[i] <= 100
"""

def countQuadruplets(nums):
    n = len(nums)
    res = 0
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                for d in range(c+1, n):
                    if nums[a] + nums[b] + nums[c] == nums[d]:
                        res += 1
    return res

# Example usage:
# print(countQuadruplets([1,2,3,6]))  # Output: 1
