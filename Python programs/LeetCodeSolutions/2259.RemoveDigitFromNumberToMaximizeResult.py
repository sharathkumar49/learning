"""
LeetCode 2259. Remove Digit From Number to Maximize Result

Given number and digit, return the maximum result after removing one occurrence of digit.

Example:
Input: number = "1231", digit = "1"
Output: "231"

Constraints:
- 2 <= number.length <= 100
- number consists of digits
"""

def removeDigit(number, digit):
    res = ''
    for i in range(len(number)):
        if number[i] == digit:
            candidate = number[:i] + number[i+1:]
            if candidate > res:
                res = candidate
    return res

# Example usage:
# print(removeDigit("1231", "1"))  # Output: "231"
