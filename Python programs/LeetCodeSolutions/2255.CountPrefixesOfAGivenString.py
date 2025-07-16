"""
LeetCode 2255. Count Prefixes of a Given String

Given words and s, return the number of words that are a prefix of s.

Example:
Input: words = ["a","b","c","ab","bc","abc"], s = "abc"
Output: 3

Constraints:
- 1 <= words.length <= 1000
- 1 <= s.length <= 10
"""

def countPrefixes(words, s):
    return sum(s.startswith(w) for w in words)

# Example usage:
# print(countPrefixes(["a","b","c","ab","bc","abc"], "abc"))  # Output: 3
