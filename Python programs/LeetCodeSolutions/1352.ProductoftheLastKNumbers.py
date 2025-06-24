"""
LeetCode 1352. Product of the Last K Numbers

Design a class ProductOfNumbers that supports adding numbers and getting the product of the last k numbers.

Constraints:
- 0 <= num <= 100
- At most 40000 calls to add and getProduct

Example:
# Not executable here as this is a class design problem for LeetCode.
"""
class ProductOfNumbers:
    def __init__(self):
        self.nums = [1]
    def add(self, num):
        if num == 0:
            self.nums = [1]
        else:
            self.nums.append(self.nums[-1] * num)
    def getProduct(self, k):
        if k >= len(self.nums):
            return 0
        return self.nums[-1] // self.nums[-k-1]

# Example usage:
# Not executable here as this is a class design problem for LeetCode.
