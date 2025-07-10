"""
LeetCode 1876. Substrings of Size Three with Distinct Characters

Given a string s, return the number of good substrings of length three. A good substring has all distinct characters.

Example:
Input: s = "xyzzaz"
Output: 1

Constraints:
- 1 <= s.length <= 100
- s consists of lowercase English letters.
"""

def countGoodSubstrings(s):
    return sum(len(set(s[i:i+3])) == 3 for i in range(len(s)-2))

# Example usage:
# print(countGoodSubstrings("xyzzaz"))  # Output: 1
