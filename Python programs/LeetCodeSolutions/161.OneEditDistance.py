"""
161. One Edit Distance
https://leetcode.com/problems/one-edit-distance/

Given two strings s and t, return true if they are one edit distance apart, otherwise return false.

Constraints:
- 0 <= s.length, t.length <= 10^4
- s and t consist of lowercase letters, uppercase letters, and digits.

Example:
Input: s = "ab", t = "acb"
Output: true
"""
def isOneEditDistance(s: str, t: str) -> bool:
    m, n = len(s), len(t)
    if abs(m - n) > 1:
        return False
    if m > n:
        return isOneEditDistance(t, s)
    for i in range(m):
        if s[i] != t[i]:
            if m == n:
                return s[i+1:] == t[i+1:]
            else:
                return s[i:] == t[i+1:]
    return m + 1 == n

# Example usage:
if __name__ == "__main__":
    print(isOneEditDistance("ab", "acb"))  # Output: True
    print(isOneEditDistance("cab", "ad"))  # Output: False
    print(isOneEditDistance("1203", "1213"))  # Output: True
