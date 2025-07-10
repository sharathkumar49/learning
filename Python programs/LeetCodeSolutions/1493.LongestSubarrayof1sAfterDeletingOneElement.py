"""
LeetCode 1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, return the length of the longest subarray containing only 1's after deleting one element.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.

Example:
Input: nums = [1,1,0,1]
Output: 3
"""
def longestSubarray(nums):
    prev = curr = res = 0
    for n in nums:
        if n == 1:
            curr += 1
        else:
            prev, curr = curr, 0
        res = max(res, prev + curr)
    return res if res < len(nums) else res - 1

# Example usage:
nums = [1,1,0,1]
print(longestSubarray(nums))  # Output: 3
