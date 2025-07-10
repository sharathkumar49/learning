"""
LeetCode 1698. Number of Distinct Substrings in a String

Given a string s, return the number of distinct non-empty substrings of s.

Example 1:
Input: s = "aabbaba"
Output: 21

Constraints:
- 1 <= s.length <= 3000
- s consists of lowercase English letters.
"""

def countDistinct(s):
    n = len(s)
    result = set()
    for i in range(n):
        for j in range(i+1, n+1):
            result.add(s[i:j])
    return len(result)

# Example usage:
# s = "aabbaba"
# print(countDistinct(s))  # Output: 21
