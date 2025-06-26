"""
LeetCode 1433. Check If a String Can Break Another String

Given two strings s1 and s2 of the same length, return true if one string can break the other (i.e., after sorting, s1[i] >= s2[i] for all i or vice versa).

Constraints:
- 1 <= s1.length == s2.length <= 10^5
- s1 and s2 consist of lowercase English letters.

Example:
Input: s1 = "abc", s2 = "xya"
Output: true
"""
def checkIfCanBreak(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    return all(a >= b for a, b in zip(s1, s2)) or all(b >= a for a, b in zip(s1, s2))

# Example usage:
s1 = "abc"
s2 = "xya"
print(checkIfCanBreak(s1, s2))  # Output: True
