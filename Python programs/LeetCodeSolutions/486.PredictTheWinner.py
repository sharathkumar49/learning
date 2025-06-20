"""
486. Predict the Winner

Given an array of scores that are non-negative integers, return True if the first player can win or tie the game, otherwise return False. Each player can choose a number from either end of the array.

Constraints:
- 1 <= nums.length <= 20
- 0 <= nums[i] <= 10^7

Example:
Input: nums = [1,5,2]
Output: False
"""

class Solution:
    def PredictTheWinner(self, nums: list) -> bool:
        def dp(i, j):
            if i == j:
                return nums[i]
            return max(nums[i] - dp(i+1, j), nums[j] - dp(i, j-1))
        return dp(0, len(nums)-1) >= 0

# Example usage:
sol = Solution()
print(sol.PredictTheWinner([1,5,2]))  # Output: False
