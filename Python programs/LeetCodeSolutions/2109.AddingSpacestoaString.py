"""
LeetCode 2109. Adding Spaces to a String

Given a string s and a list of indices, return the string with spaces added at the given indices.

Example:
Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
Output: "Leetcode Helps Me Learn"

Constraints:
- 1 <= s.length <= 3 * 10^5
- 1 <= spaces.length <= 3 * 10^5
"""

def addSpaces(s, spaces):
    res = []
    j = 0
    for i in range(len(s)):
        if j < len(spaces) and i == spaces[j]:
            res.append(' ')
            j += 1
        res.append(s[i])
    return ''.join(res)

# Example usage:
# print(addSpaces("LeetcodeHelpsMeLearn", [8,13,15]))  # Output: "Leetcode Helps Me Learn"
