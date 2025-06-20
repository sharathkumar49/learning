"""
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Constraints:
- 1 <= s.length <= 5 * 10^4
- t.length == s.length
- s and t consist of any valid ascii character.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
"""
def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    s2t, t2s = {}, {}
    for a, b in zip(s, t):
        if (a in s2t and s2t[a] != b) or (b in t2s and t2s[b] != a):
            return False
        s2t[a] = b
        t2s[b] = a
    return True

# Example usage:
if __name__ == "__main__":
    print(isIsomorphic("egg", "add"))      # Output: True
    print(isIsomorphic("foo", "bar"))      # Output: False
    print(isIsomorphic("paper", "title"))  # Output: True
