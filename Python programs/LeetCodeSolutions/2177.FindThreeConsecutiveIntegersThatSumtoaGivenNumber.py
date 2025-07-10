"""
LeetCode 2177. Find Three Consecutive Integers That Sum to a Given Number

Given an integer num, return three consecutive integers (as a list) that sum to num. If no such answer exists, return an empty list.

Example:
Input: num = 33
Output: [10,11,12]

Constraints:
- 0 <= num <= 10^{15}
"""

def sumOfThree(num):
    if num % 3 != 0:
        return []
    x = num // 3
    return [x-1, x, x+1]

# Example usage:
# print(sumOfThree(33))  # Output: [10,11,12]
