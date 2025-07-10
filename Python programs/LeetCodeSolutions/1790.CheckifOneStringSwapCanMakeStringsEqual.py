"""
LeetCode 1790. Check if One String Swap Can Make Strings Equal

Given two strings s1 and s2, return true if you can make them equal by swapping two letters in s1 exactly once.

Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true

Constraints:
- 1 <= s1.length, s2.length <= 100
- s1.length == s2.length
- s1 and s2 consist of lowercase English letters
"""

def areAlmostEqual(s1, s2):
    diff = [(a, b) for a, b in zip(s1, s2) if a != b]
    return not diff or (len(diff) == 2 and diff[0] == diff[1][::-1])

# Example usage:
# s1 = "bank"
# s2 = "kanb"
# print(areAlmostEqual(s1, s2))  # Output: True
