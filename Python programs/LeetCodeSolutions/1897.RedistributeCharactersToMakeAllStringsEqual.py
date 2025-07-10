"""
LeetCode 1897. Redistribute Characters to Make All Strings Equal

Given an array of strings words, return true if you can redistribute characters so that all strings are equal.

Example:
Input: words = ["abc","aabc","bc"]
Output: true

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of lowercase English letters.
"""

from collections import Counter

def makeEqual(words):
    count = Counter(''.join(words))
    n = len(words)
    return all(v % n == 0 for v in count.values())

# Example usage:
# print(makeEqual(["abc","aabc","bc"]))  # Output: True
