"""
491. Increasing Subsequences

Given an integer array nums, return all the different possible increasing subsequences of the given array with at least two elements.

Constraints:
- 1 <= nums.length <= 15
- -100 <= nums[i] <= 100

Example:
Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
"""

class Solution:
    def findSubsequences(self, nums: list) -> list:
        res = set()
        def dfs(start, path):
            if len(path) > 1:
                res.add(tuple(path))
            for i in range(start, len(nums)):
                if not path or nums[i] >= path[-1]:
                    dfs(i+1, path + [nums[i]])
        dfs(0, [])
        return [list(seq) for seq in res]

# Example usage:
sol = Solution()
print(sol.findSubsequences([4,6,7,7]))  # Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
