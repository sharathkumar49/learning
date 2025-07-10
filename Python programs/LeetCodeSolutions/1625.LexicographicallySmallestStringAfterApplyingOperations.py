"""
LeetCode 1625. Lexicographically Smallest String After Applying Operations

Given a string s of even length, and two integers a and b, you can perform two operations any number of times:
- Add a to all odd indices (modulo 10).
- Rotate the string to the right by b positions.
Return the lexicographically smallest string you can obtain.

Example 1:
Input: s = "5525", a = 9, b = 2
Output: "2050"

Constraints:
- 2 <= s.length <= 100
- s.length is even
- 0 <= a <= 9
- 1 <= b <= s.length - 1
"""

def findLexSmallestString(s, a, b):
    from collections import deque
    seen = set()
    q = deque([s])
    res = s
    while q:
        cur = q.popleft()
        if cur < res:
            res = cur
        t = list(cur)
        for i in range(1, len(t), 2):
            t[i] = str((int(t[i]) + a) % 10)
        t1 = ''.join(t)
        t2 = cur[-b:] + cur[:-b]
        for nxt in [t1, t2]:
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return res

# Example usage:
# s = "5525"
# a = 9
# b = 2
# print(findLexSmallestString(s, a, b))  # Output: "2050"
