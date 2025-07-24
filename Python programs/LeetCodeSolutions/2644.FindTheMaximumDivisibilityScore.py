"""
LeetCode 2644. Find the Maximum Divisibility Score

Given nums and divisors, return the divisor with the maximum divisibility score.

Constraints:
- 1 <= nums.length, divisors.length <= 100
"""

def maxDivScore(nums, divisors):
    return max(divisors, key=lambda d: (sum(x%d==0 for x in nums), -d))
# Example usage:
# print(maxDivScore([4,7,9,3,9], [5,2,3]))  # Output: 3
