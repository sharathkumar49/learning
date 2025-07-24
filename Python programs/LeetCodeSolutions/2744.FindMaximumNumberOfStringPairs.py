"""
LeetCode 2744. Find Maximum Number of String Pairs

Given words, return the maximum number of string pairs.

Constraints:
- 1 <= words.length <= 100
"""

def maximumNumberOfStringPairs(words):
    s = set()
    res = 0
    for w in words:
        if w[::-1] in s:
            res += 1
        s.add(w)
    return res
# Example usage:
# print(maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]))  # Output: 2
