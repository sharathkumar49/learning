"""
LeetCode 679. 24 Game

You are given an array of four integers. Each integer is between 1 and 9, inclusive. You have to judge whether they can get the value 24.

You can operate as many times as you want with the following operations: addition, subtraction, multiplication, and division.

Example 1:
Input: [4,1,8,7]
Output: true
Explanation: (8-4) * (7-1) = 24

Example 2:
Input: [1,2,1,2]
Output: false

Constraints:
- The input consists of exactly four integers.
- 1 <= nums[i] <= 9
"""
from typing import List

def judgePoint24(nums: List[int]) -> bool:
    def dfs(nums):
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    for op in [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y if y != 0 else float('inf')]:
                        val = op(nums[i], nums[j])
                        if dfs(next_nums + [val]):
                            return True
        return False
    return dfs(list(map(float, nums)))

# Example usage
if __name__ == "__main__":
    print(judgePoint24([4,1,8,7]))  # Output: True
    print(judgePoint24([1,2,1,2]))  # Output: False
