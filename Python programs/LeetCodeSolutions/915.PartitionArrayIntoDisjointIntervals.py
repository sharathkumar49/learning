"""
915. Partition Array into Disjoint Intervals
https://leetcode.com/problems/partition-array-into-disjoint-intervals/

Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:
- Every element in left is less than or equal to every element in right.
- left and right are non-empty.
- left has the smallest possible size.
Return the length of left after such a partitioning.

Constraints:
- 2 <= nums.length <= 30000
- 0 <= nums[i] <= 10^6

Example:
Input: nums = [5,0,3,8,6]
Output: 3
"""
from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        max_left = [0]*n
        min_right = [0]*n
        max_left[0] = nums[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], nums[i])
        min_right[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            min_right[i] = min(min_right[i+1], nums[i])
        for i in range(n-1):
            if max_left[i] <= min_right[i+1]:
                return i+1
        return -1

# Example usage
if __name__ == "__main__":
    nums = [5,0,3,8,6]
    print(Solution().partitionDisjoint(nums))  # Output: 3
