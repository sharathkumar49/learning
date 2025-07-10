"""
LeetCode 2051. The Number of Distinct Substrings in a String

Given a string s, return the number of distinct non-empty substrings of s.

Example:
Input: s = "abc"
Output: 6

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.
"""

def distinctSubstring(s):
    n = len(s)
    substrings = set()
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.add(s[i:j])
    return len(substrings)

# Example usage:
# print(distinctSubstring("abc"))  # Output: 6
