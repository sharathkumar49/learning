"""
LeetCode 2752. Sum of Squares of Special Elements

Given nums, return the sum of squares of special elements.

Constraints:
- 1 <= nums.length <= 100
"""

def sumOfSquares(nums):
    n = len(nums)
    return sum(x*x for i, x in enumerate(nums, 1) if n % i == 0)
# Example usage:
# print(sumOfSquares([1,2,3,4]))  # Output: 21
