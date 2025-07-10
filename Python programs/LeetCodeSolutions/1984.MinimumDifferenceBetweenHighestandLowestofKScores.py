"""
LeetCode 1984. Minimum Difference Between Highest and Lowest of K Scores

Given an array nums and an integer k, return the minimum difference between the highest and lowest scores of any k students.

Example:
Input: nums = [90], k = 1
Output: 0

Constraints:
- 1 <= k <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5
"""

def minimumDifference(nums, k):
    nums.sort()
    return min(nums[i+k-1] - nums[i] for i in range(len(nums)-k+1))

# Example usage:
# print(minimumDifference([90], 1))  # Output: 0
