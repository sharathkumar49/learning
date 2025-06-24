"""
LeetCode 1347. Minimum Number of Steps to Make Two Strings Anagram

Given two strings s and t of equal length, return the minimum number of steps to make t an anagram of s. In one step, you can replace any character in t with another character.

Constraints:
- 1 <= s.length <= 5 * 10^4
- s.length == t.length
- s and t consist of lowercase English letters only.

Example:
Input: s = "bab", t = "aba"
Output: 1
"""
def minSteps(s, t):
    from collections import Counter
    c1, c2 = Counter(s), Counter(t)
    return sum((c1 - c2).values())

# Example usage:
s = "bab"
t = "aba"
print(minSteps(s, t))  # Output: 1
