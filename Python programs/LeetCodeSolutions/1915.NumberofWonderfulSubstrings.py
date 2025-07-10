"""
LeetCode 1915. Number of Wonderful Substrings

Given a string word, return the number of wonderful substrings. A wonderful substring is a substring where at most one letter appears an odd number of times.

Example:
Input: word = "aba"
Output: 4

Constraints:
- 1 <= word.length <= 10^5
- word consists of lowercase English letters.
"""

def wonderfulSubstrings(word):
    from collections import Counter
    res = 0
    mask = 0
    count = Counter([0])
    for c in word:
        mask ^= 1 << (ord(c) - ord('a'))
        res += count[mask]
        for i in range(10):
            res += count[mask ^ (1 << i)]
        count[mask] += 1
    return res

# Example usage:
# print(wonderfulSubstrings("aba"))  # Output: 4
