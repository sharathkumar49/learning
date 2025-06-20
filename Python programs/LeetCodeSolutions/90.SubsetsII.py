"""
90. Subsets II
https://leetcode.com/problems/subsets-ii/

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10

Example:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""
from typing import List

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    def backtrack(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0, [])
    return res

# Example usage:
if __name__ == "__main__":
    print(subsetsWithDup([1,2,2]))  # Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
