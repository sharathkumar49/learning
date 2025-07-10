"""
LeetCode 1941. Check if All Characters Have Equal Number of Occurrences

Given a string s, return true if all characters have the same number of occurrences.

Example:
Input: s = "abacbc"
Output: true

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.
"""

def areOccurrencesEqual(s):
    from collections import Counter
    vals = list(Counter(s).values())
    return min(vals) == max(vals)

# Example usage:
# print(areOccurrencesEqual("abacbc"))  # Output: True
