"""
258. Add Digits
https://leetcode.com/problems/add-digits/

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Constraints:
- 0 <= num <= 2^31 - 1

Example 1:
Input: num = 38
Output: 2

Example 2:
Input: num = 0
Output: 0
"""
def addDigits(num):
    if num == 0:
        return 0
    return 1 + (num - 1) % 9

# Example usage:
if __name__ == "__main__":
    print(addDigits(38))  # Output: 2
    print(addDigits(0))   # Output: 0
