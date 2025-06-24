"""
LeetCode 1283. Find the Smallest Divisor Given a Threshold

Given an array of integers nums and an integer threshold, return the smallest divisor such that the sum of the division results (rounded up) is less than or equal to threshold.

Constraints:
- 1 <= nums.length <= 5 * 10^4
- 1 <= nums[i] <= 10^6
- nums.length <= threshold <= 10^6

Example:
Input: nums = [1,2,5,9], threshold = 6
Output: 5
"""
def smallestDivisor(nums, threshold):
    import math
    left, right = 1, max(nums)
    while left < right:
        mid = (left + right) // 2
        total = sum((x + mid - 1) // mid for x in nums)
        if total > threshold:
            left = mid + 1
        else:
            right = mid
    return left

# Example usage:
nums = [1,2,5,9]
threshold = 6
print(smallestDivisor(nums, threshold))  # Output: 5
