"""
LeetCode 1509. Minimum Difference Between Largest and Smallest Value in Three Moves

Given an array nums, you can make at most three moves. Return the minimum difference between the largest and smallest value of nums after at most three moves.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Example:
Input: nums = [5,3,2,4]
Output: 0
"""
def minDifference(nums):
    nums.sort()
    n = len(nums)
    if n <= 4:
        return 0
    return min(nums[-1-i] - nums[3-i] for i in range(4))

# Example usage:
nums = [5,3,2,4]
print(minDifference(nums))  # Output: 0
