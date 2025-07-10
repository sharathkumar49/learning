"""
LeetCode 1957. Delete Characters to Make Fancy String

Given a string s, return the fancy string after deleting characters so that no three consecutive characters are the same.

Example:
Input: s = "leeetcode"
Output: "leetcode"

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
"""

def makeFancyString(s):
    res = []
    for c in s:
        if len(res) >= 2 and res[-1] == res[-2] == c:
            continue
        res.append(c)
    return ''.join(res)

# Example usage:
# print(makeFancyString("leeetcode"))  # Output: "leetcode"
