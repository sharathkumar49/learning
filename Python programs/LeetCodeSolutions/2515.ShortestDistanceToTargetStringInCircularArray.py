"""
LeetCode 2515. Shortest Distance to Target String in a Circular Array

Given a circular array and a target, return the shortest distance to the target.

Constraints:
- 1 <= words.length <= 10^5
"""

def shortestDistance(words, target, start):
    n = len(words)
    res = n
    for i in range(n):
        if words[i] == target:
            res = min(res, min(abs(i-start), n-abs(i-start)))
    return res
# Example usage:
# print(shortestDistance(["a","b","c","d","e"], "e", 2))  # Output: 2
