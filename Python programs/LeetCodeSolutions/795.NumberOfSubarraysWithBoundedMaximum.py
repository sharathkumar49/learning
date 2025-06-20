"""
795. Number of Subarrays with Bounded Maximum

Given an integer array nums and two integers left and right, return the number of contiguous, non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

Example 1:
Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3

Example 2:
Input: nums = [2,9,2,5,6], left = 2, right = 8
Output: 7

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
- 0 <= left <= right <= 10^9
"""
def numSubarrayBoundedMax(nums, left, right):
    def count(bound):
        ans = cur = 0
        for x in nums:
            cur = cur + 1 if x <= bound else 0
            ans += cur
        return ans
    return count(right) - count(left - 1)

# Example usage:
print(numSubarrayBoundedMax([2,1,4,3], 2, 3))  # Output: 3
print(numSubarrayBoundedMax([2,9,2,5,6], 2, 8))  # Output: 7
