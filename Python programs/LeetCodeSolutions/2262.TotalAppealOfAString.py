"""
LeetCode 2262. Total Appeal of A String

Given a string s, return the total appeal of all substrings.

Example:
Input: s = "abbca"
Output: 28

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters
"""

def appealSum(s):
    last = {}
    res = 0
    curr = 0
    for i, c in enumerate(s):
        curr += i - last.get(c, -1)
        res += curr
        last[c] = i
    return res

# Example usage:
# print(appealSum("abbca"))  # Output: 28
