"""
LeetCode 2520. Count the Digits That Divide a Number

Given an integer num, return the number of digits that divide num.

Constraints:
- 1 <= num <= 10^9
"""

def countDigits(num):
    return sum(num%int(d)==0 for d in str(num))
# Example usage:
# print(countDigits(1248))  # Output: 4
