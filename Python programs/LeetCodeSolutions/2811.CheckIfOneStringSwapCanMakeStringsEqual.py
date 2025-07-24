"""
LeetCode 2811. Check if One String Swap Can Make Strings Equal

Given s1 and s2, return True if one swap can make them equal.

Constraints:
- 1 <= s1.length, s2.length <= 100
"""

def areAlmostEqual(s1, s2):
    diff = [(a, b) for a, b in zip(s1, s2) if a != b]
    return len(diff) == 0 or (len(diff) == 2 and diff[0] == diff[1][::-1])
# Example usage:
# print(areAlmostEqual("bank", "kanb"))  # Output: True
