"""
LeetCode 1910. Remove All Occurrences of a Substring

Given two strings s and part, remove all occurrences of part in s.

Example:
Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"

Constraints:
- 1 <= s.length <= 1000
- 1 <= part.length <= 1000
- s and part consist of lowercase English letters.
"""

def removeOccurrences(s, part):
    while part in s:
        s = s.replace(part, "")
    return s

# Example usage:
# print(removeOccurrences("daabcbaabcbc", "abc"))  # Output: "dab"
