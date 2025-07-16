"""
LeetCode 2294. Partition Array Such That Maximum Difference Is K

Given nums and k, return the minimum number of subarrays such that the difference between the maximum and minimum in each subarray is at most k.

Example:
Input: nums = [3,6,1,2,5], k = 2
Output: 2

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= k <= 10^9
"""

def partitionArray(nums, k):
    nums.sort()
    res = 1
    start = nums[0]
    for num in nums:
        if num - start > k:
            res += 1
            start = num
    return res

# Example usage:
# print(partitionArray([3,6,1,2,5], 2))  # Output: 2
