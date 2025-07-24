"""
LeetCode 2695. Array Wrapper

Implement an array wrapper class with valueOf and toString methods.

Constraints:
- 1 <= arr.length <= 10^5
"""
class ArrayWrapper:
    def __init__(self, nums):
        self.nums = nums
    def __add__(self, other):
        return sum(self.nums) + sum(other.nums)
    def __str__(self):
        return str(self.nums)
# Example usage:
# obj1 = ArrayWrapper([1,2])
# obj2 = ArrayWrapper([3,4])
# print(obj1 + obj2)  # Output: 10
# print(str(obj1))    # Output: [1, 2]
