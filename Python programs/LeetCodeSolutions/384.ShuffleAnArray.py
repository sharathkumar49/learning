"""
384. Shuffle an Array

Implement the Solution class:
- Solution(int[] nums) Initializes the object with the integer array nums.
- int[] reset() Resets the array to its original configuration and returns it.
- int[] shuffle() Returns a random shuffling of the array.

Constraints:
- 1 <= nums.length <= 200
- -10^6 <= nums[i] <= 10^6
- All the elements of nums are unique.
- At most 5 * 10^4 calls will be made to reset and shuffle.
"""
import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.nums = nums[:]
    def reset(self) -> List[int]:
        self.nums = self.original[:]
        return self.nums
    def shuffle(self) -> List[int]:
        arr = self.nums[:]
        random.shuffle(arr)
        return arr

# Example usage:
nums = [1,2,3]
obj = Solution(nums)
print(obj.shuffle())  # Output: [3,1,2] (random)
print(obj.reset())    # Output: [1,2,3]
print(obj.shuffle())  # Output: [2,3,1] (random)
