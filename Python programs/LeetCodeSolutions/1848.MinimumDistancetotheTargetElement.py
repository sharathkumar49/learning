"""
LeetCode 1848. Minimum Distance to the Target Element

Given an integer array nums and an integer target, return the minimum distance from any index i such that nums[i] == target to the given start index. Return -1 if target is not in nums.

Example 1:
Input: nums = [1,2,3,4,5], target = 5, start = 3
Output: 1

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^4
- 0 <= start < nums.length
"""

def getMinDistance(nums, target, start):
    ans = float('inf')
    for i, v in enumerate(nums):
        if v == target:
            ans = min(ans, abs(i - start))
    return ans if ans != float('inf') else -1

# Example usage:
# nums = [1,2,3,4,5]
# target = 5
# start = 3
# print(getMinDistance(nums, target, start))  # Output: 1
