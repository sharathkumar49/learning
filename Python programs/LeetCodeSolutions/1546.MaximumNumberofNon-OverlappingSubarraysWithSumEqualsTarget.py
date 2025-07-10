"""
LeetCode 1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target

Given an array nums and an integer target, return the maximum number of non-overlapping subarrays that sum to target.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= target <= 10^6

Example:
Input: nums = [1,1,1,1,1], target = 2
Output: 2
"""
def maxNonOverlapping(nums, target):
    seen = set([0])
    res = s = 0
    for x in nums:
        s += x
        if s - target in seen:
            res += 1
            s = 0
            seen = set([0])
        else:
            seen.add(s)
    return res

# Example usage:
nums = [1,1,1,1,1]
target = 2
print(maxNonOverlapping(nums, target))  # Output: 2
