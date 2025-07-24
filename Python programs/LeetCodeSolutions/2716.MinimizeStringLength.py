"""
LeetCode 2716. Minimize String Length

Given s, return the minimum possible length after removing duplicate characters.

Constraints:
- 1 <= s.length <= 100
"""

def minimizedStringLength(s):
    return len(set(s))
# Example usage:
# print(minimizedStringLength("aaabc"))  # Output: 3
