"""
LeetCode 1961. Check If String Is a Prefix of Array

Given a string s and an array of strings words, return true if s is a prefix string of words.

Example:
Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true

Constraints:
- 1 <= s.length <= 100
- 1 <= words.length <= 100
- 1 <= words[i].length <= 20
- s and words[i] consist of lowercase English letters.
"""

def isPrefixString(s, words):
    t = ''
    for w in words:
        t += w
        if t == s:
            return True
        if len(t) > len(s):
            break
    return False

# Example usage:
# print(isPrefixString("iloveleetcode", ["i","love","leetcode","apples"]))  # Output: True
