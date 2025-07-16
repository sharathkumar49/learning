"""
LeetCode 2302. Count Subarrays With Score Less Than K

Given nums and k, return the number of subarrays with score less than k.

Example:
Input: nums = [2,1,4,3,5], k = 10
Output: 6

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

def countSubarrays(nums, k):
    res = left = curr = 0
    for right, num in enumerate(nums):
        curr += num
        while curr * (right-left+1) >= k:
            curr -= nums[left]
            left += 1
        res += right-left+1
    return res

# Example usage:
# print(countSubarrays([2,1,4,3,5], 10))  # Output: 6
