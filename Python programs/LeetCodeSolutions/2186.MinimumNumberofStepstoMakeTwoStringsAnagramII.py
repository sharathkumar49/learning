"""
LeetCode 2186. Minimum Number of Steps to Make Two Strings Anagram II

Given two strings s and t, return the minimum number of steps to make s and t anagrams of each other. In one step, you can delete a character from either string.

Example:
Input: s = "leetcode", t = "coats"
Output: 7

Constraints:
- 1 <= s.length, t.length <= 10^5
- s and t consist of lowercase English letters.
"""

def minSteps(s, t):
    from collections import Counter
    cs, ct = Counter(s), Counter(t)
    return sum((cs - ct).values()) + sum((ct - cs).values())

# Example usage:
# print(minSteps("leetcode", "coats"))  # Output: 7
