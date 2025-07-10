"""
LeetCode 2134. Minimum Swaps to Group All 1's Together II

Given a binary array nums, return the minimum number of swaps to group all 1's together in a circular array.

Example:
Input: nums = [0,1,0,1,1,0,0]
Output: 1

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is 0 or 1
"""

def minSwaps(nums):
    n = len(nums)
    ones = sum(nums)
    nums += nums[:ones-1]
    curr = max_ones = sum(nums[:ones])
    for i in range(ones, len(nums)):
        curr += nums[i] - nums[i-ones]
        max_ones = max(max_ones, curr)
    return ones - max_ones

# Example usage:
# print(minSwaps([0,1,0,1,1,0,0]))  # Output: 1
