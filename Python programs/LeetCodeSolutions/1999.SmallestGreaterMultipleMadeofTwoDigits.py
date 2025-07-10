"""
LeetCode 1999. Smallest Greater Multiple Made of Two Digits

Given two digits d1 and d2, and an integer n, return the smallest integer greater than n that consists only of d1 and d2.

Example:
Input: d1 = 1, d2 = 2, n = 10
Output: 12

Constraints:
- 0 <= d1, d2 <= 9
- 1 <= n <= 10^9
"""

def findSmallest(d1, d2, n):
    from collections import deque
    digits = sorted({str(d1), str(d2)})
    q = deque(digits)
    while q:
        s = q.popleft()
        x = int(s)
        if x > n:
            return x
        for d in digits:
            q.append(s + d)

# Example usage:
# print(findSmallest(1, 2, 10))  # Output: 12
