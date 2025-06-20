"""
503. Next Greater Element II

Given a circular array, return the next greater number for every element. If it doesn't exist, return -1 for that number.

Constraints:
- 1 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9

Example:
Input: nums = [1,2,1]
Output: [2,-1,2]
"""

class Solution:
    def nextGreaterElements(self, nums: list) -> list:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2*n):
            while stack and nums[i % n] > nums[stack[-1]]:
                res[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)
        return res

# Example usage:
sol = Solution()
print(sol.nextGreaterElements([1,2,1]))  # Output: [2, -1, 2]
