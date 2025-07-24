"""
LeetCode 2687. Find the Value of the Partition

Given nums, return the value of the partition.

Constraints:
- 2 <= nums.length <= 10^5
"""

def findValueOfPartition(nums):
    nums.sort()
    return min(nums[i+1]-nums[i] for i in range(len(nums)-1))
# Example usage:
# print(findValueOfPartition([1,3,6,19,20]))  # Output: 2
