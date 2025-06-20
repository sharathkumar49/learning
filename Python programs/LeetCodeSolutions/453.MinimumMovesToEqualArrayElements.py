"""
453. Minimum Moves to Equal Array Elements

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Constraints:
- n == nums.length
- 1 <= n <= 10^5
- -10^9 <= nums[i] <= 10^9
- The answer is guaranteed to fit in a 32-bit integer.

Example:
Input: nums = [1,2,3]
Output: 3
"""

class Solution:
    def minMoves(self, nums: list) -> int:
        return sum(nums) - min(nums) * len(nums)

# Example usage:
sol = Solution()
print(sol.minMoves([1,2,3]))  # Output: 3
