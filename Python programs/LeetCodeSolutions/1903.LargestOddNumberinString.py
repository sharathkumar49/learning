"""
LeetCode 1903. Largest Odd Number in String

Given a string num, return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string if no such integer exists.

Example:
Input: num = "52"
Output: "5"

Constraints:
- 1 <= num.length <= 10^5
- num consists only of digits.
"""

def largestOddNumber(num):
    for i in range(len(num)-1, -1, -1):
        if int(num[i]) % 2:
            return num[:i+1]
    return ""

# Example usage:
# print(largestOddNumber("52"))  # Output: "5"
