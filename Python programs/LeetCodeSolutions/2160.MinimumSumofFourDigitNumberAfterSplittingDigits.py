"""
LeetCode 2160. Minimum Sum of Four Digit Number After Splitting Digits

Given a four-digit number num, split its digits into two new numbers such that the sum is minimized. Return the minimum possible sum.

Example:
Input: num = 2932
Output: 52

Constraints:
- 1000 <= num <= 9999
"""

def minimumSum(num):
    digits = sorted([int(x) for x in str(num)])
    return digits[0]*10 + digits[2] + digits[1]*10 + digits[3]

# Example usage:
# print(minimumSum(2932))  # Output: 52
