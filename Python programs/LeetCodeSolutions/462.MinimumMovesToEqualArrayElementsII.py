"""
462. Minimum Moves to Equal Array Elements II

Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal, where a move is incrementing or decrementing a selected element by 1.

Constraints:
- n == nums.length
- 1 <= n <= 10^5
- -10^9 <= nums[i] <= 10^9

Example:
Input: nums = [1,2,3]
Output: 2
"""

class Solution:
    def minMoves2(self, nums: list) -> int:
        nums.sort()
        median = nums[len(nums)//2]
        return sum(abs(num - median) for num in nums)

# Example usage:
sol = Solution()
print(sol.minMoves2([1,2,3]))  # Output: 2
