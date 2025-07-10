"""
LeetCode 2185. Counting Words With a Given Prefix

Given an array of strings words and a string pref, return the number of strings in words that start with pref.

Example:
Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length, pref.length <= 100
- words[i] and pref consist of lowercase English letters.
"""

def prefixCount(words, pref):
    return sum(w.startswith(pref) for w in words)

# Example usage:
# print(prefixCount(["pay","attention","practice","attend"], "at"))  # Output: 2
