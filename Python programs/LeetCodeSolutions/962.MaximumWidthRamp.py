"""
962. Maximum Width Ramp
https://leetcode.com/problems/maximum-width-ramp/

A ramp in an array is a pair (i, j) for i < j such that nums[i] <= nums[j]. The width of such a ramp is j - i. Return the maximum width of a ramp in nums.

Constraints:
- 2 <= nums.length <= 5 * 10^4
- 0 <= nums[i] <= 5 * 10^4

Example:
Input: nums = [6,0,8,2,1,5]
Output: 4
"""
from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, x in enumerate(nums):
            if not stack or nums[stack[-1]] > x:
                stack.append(i)
        res = 0
        for j in reversed(range(len(nums))):
            while stack and nums[stack[-1]] <= nums[j]:
                res = max(res, j - stack.pop())
        return res

# Example usage
if __name__ == "__main__":
    nums = [6,0,8,2,1,5]
    print(Solution().maxWidthRamp(nums))  # Output: 4
