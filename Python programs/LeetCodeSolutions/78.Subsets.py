"""
78. Subsets
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.

Example:
Input: nums = [1,2,3]
Output: [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]
"""
from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    def backtrack(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0, [])
    return res

# Example usage:
if __name__ == "__main__":
    print(subsets([1,2,3]))  # Output: [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]
