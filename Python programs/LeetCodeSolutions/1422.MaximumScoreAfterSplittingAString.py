"""
LeetCode 1422. Maximum Score After Splitting a String

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings. The score is the number of zeros in the left substring plus the number of ones in the right substring.

Constraints:
- 2 <= s.length <= 500
- s consists of '0' and '1'.

Example:
Input: s = "011101"
Output: 5
"""
def maxScore(s):
    max_score = 0
    for i in range(1, len(s)):
        left = s[:i].count('0')
        right = s[i:].count('1')
        max_score = max(max_score, left + right)
    return max_score

# Example usage:
s = "011101"
print(maxScore(s))  # Output: 5
