"""
LeetCode 1585. Check If String Is Transformable With Substring Sort Operations

Given two strings s and t of the same length, return true if s can be transformed into t using any number of moves. In one move, you can choose any substring of s and sort it in ascending order.

Example 1:
Input: s = "84532", t = "34852"
Output: true

Example 2:
Input: s = "34521", t = "23415"
Output: true

Constraints:
- 1 <= s.length == t.length <= 10^5
- s and t consist of only digits.
"""

from collections import deque

def isTransformable(s, t):
    pos = [deque() for _ in range(10)]
    for i, c in enumerate(s):
        pos[int(c)].append(i)
    for c in t:
        d = int(c)
        if not pos[d]:
            return False
        idx = pos[d].popleft()
        for smaller in range(d):
            if pos[smaller] and pos[smaller][0] < idx:
                return False
    return True

# Example usage:
# s = "84532"
# t = "34852"
# print(isTransformable(s, t))  # Output: True
