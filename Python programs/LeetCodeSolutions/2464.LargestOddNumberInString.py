"""
LeetCode 2464. Largest Odd Number in String

Given a string num, return the largest odd number that is a non-empty substring.

Constraints:
- 1 <= num.length <= 10^5
"""

def largestOddNumber(num):
    for i in range(len(num)-1, -1, -1):
        if int(num[i])%2:
            return num[:i+1]
    return ''

# Example usage:
# print(largestOddNumber("52"))  # Output: "5"
