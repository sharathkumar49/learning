"""
456. 132 Pattern

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j], nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
Return true if there is a 132 pattern in nums, otherwise, return false.

Constraints:
- n == nums.length
- 1 <= n <= 2 * 10^5
- -10^9 <= nums[i] <= 10^9

Example:
Input: nums = [1,2,3,4]
Output: False
"""

class Solution:
    def find132pattern(self, nums: list) -> bool:
        stack = []
        s3 = float('-inf')
        for n in reversed(nums):
            if n < s3:
                return True
            while stack and n > stack[-1]:
                s3 = stack.pop()
            stack.append(n)
        return False

# Example usage:
sol = Solution()
print(sol.find132pattern([1,2,3,4]))  # Output: False
