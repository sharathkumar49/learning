"""
LeetCode 2243. Calculate Digit Sum of a String

Given a string s and integer k, return the digit sum string.

Example:
Input: s = "11111222223", k = 3
Output: "135"

Constraints:
- 1 <= s.length <= 100
- 1 <= k <= 100
"""

def digitSum(s, k):
    while len(s) > k:
        t = ''
        for i in range(0, len(s), k):
            t += str(sum(int(x) for x in s[i:i+k]))
        s = t
    return s

# Example usage:
# print(digitSum("11111222223", 3))  # Output: "135"
