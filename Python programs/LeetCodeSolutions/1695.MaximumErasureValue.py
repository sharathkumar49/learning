"""
LeetCode 1695. Maximum Erasure Value

You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

Example 1:
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
"""

def maximumUniqueSubarray(nums):
    seen = set()
    left = 0
    curr_sum = 0
    max_sum = 0
    for right in range(len(nums)):
        while nums[right] in seen:
            seen.remove(nums[left])
            curr_sum -= nums[left]
            left += 1
        seen.add(nums[right])
        curr_sum += nums[right]
        max_sum = max(max_sum, curr_sum)
    return max_sum

# Example usage:
# nums = [4,2,4,5,6]
# print(maximumUniqueSubarray(nums))  # Output: 17
