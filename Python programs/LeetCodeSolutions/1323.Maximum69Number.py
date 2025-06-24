"""
LeetCode 1323. Maximum 69 Number

Given a positive integer num consisting only of digits 6 and 9, return the maximum number you can get by changing at most one digit (6 becomes 9, or 9 becomes 6).

Constraints:
- 1 <= num <= 10^4
- num consists only of 6 and 9 digits.

Example:
Input: num = 9669
Output: 9969
"""
def maximum69Number(num):
    return int(str(num).replace('6', '9', 1))

# Example usage:
num = 9669
print(maximum69Number(num))  # Output: 9969
