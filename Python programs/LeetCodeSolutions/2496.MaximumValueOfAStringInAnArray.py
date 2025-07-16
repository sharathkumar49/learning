"""
LeetCode 2496. Maximum Value of a String in an Array

Given an array of strings, return the maximum value (length or integer value).

Constraints:
- 1 <= strs.length <= 100
"""

def maximumValue(strs):
    return max(int(s) if s.isdigit() else len(s) for s in strs)

# Example usage:
# print(maximumValue(["alic3","bob","3","4","00000"]))  # Output: 5
