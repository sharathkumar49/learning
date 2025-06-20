"""
398. Random Pick Index

Given an integer array nums with possible duplicates, implement the Solution class:
- Solution(int[] nums) Initializes the object with the array nums.
- int pick(int target) Picks a random index i where nums[i] == target. Each index should have equal probability of being returned.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -2^31 <= nums[i] <= 2^31 - 1
- target is guaranteed to be in nums.
- At most 10^4 calls will be made to pick.
"""
import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.idx = {}
        for i, num in enumerate(nums):
            if num not in self.idx:
                self.idx[num] = []
            self.idx[num].append(i)
    def pick(self, target: int) -> int:
        return random.choice(self.idx[target])

# Example usage:
nums = [1,2,3,3,3]
obj = Solution(nums)
print(obj.pick(3))  # Output: 2, 3, or 4 (random)
