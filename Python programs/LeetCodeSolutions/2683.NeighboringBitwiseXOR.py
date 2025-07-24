"""
LeetCode 2683. Neighboring Bitwise XOR

Given s, return True if the string can be constructed with the given XOR property.

Constraints:
- 1 <= s.length <= 10^5
"""

def doesValidArrayExist(derived):
    return sum(derived) % 2 == 0
# Example usage:
# print(doesValidArrayExist([1,1,0]))  # Output: True
