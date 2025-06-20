"""
307. Range Sum Query - Mutable

Given an integer array nums, handle multiple queries of the following types:
- Update the value of an element in nums.
- Calculate the sum of the elements of nums between indices left and right inclusive.

Implement the NumArray class:
- NumArray(int[] nums) Initializes the object with the integer array nums.
- void update(int index, int val) Updates the value of nums[index] to be val.
- int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- 0 <= index < nums.length
- 0 <= left <= right < nums.length
- At most 3 * 10^4 calls will be made to update and sumRange.
"""
from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        self.nums = nums[:]
        for i in range(self.n):
            self._add(i + 1, nums[i])

    def _add(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, diff)

    def _sum(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def sumRange(self, left: int, right: int) -> int:
        return self._sum(right + 1) - self._sum(left)

# Example usage:
nums = [1, 3, 5]
obj = NumArray(nums)
print(obj.sumRange(0, 2))  # Output: 9
obj.update(1, 2)
print(obj.sumRange(0, 2))  # Output: 8
