"""
LeetCode 2264. Largest 3-Same-Digit Number in String

Given a string num, return the largest 3-same-digit number in it.

Example:
Input: num = "6777133339"
Output: "777"

Constraints:
- 3 <= num.length <= 100
"""

def largestGoodInteger(num):
    res = ''
    for i in range(len(num)-2):
        if num[i] == num[i+1] == num[i+2]:
            res = max(res, num[i]*3)
    return res

# Example usage:
# print(largestGoodInteger("6777133339"))  # Output: "777"
