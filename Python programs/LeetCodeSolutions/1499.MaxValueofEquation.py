"""
LeetCode 1499. Max Value of Equation

Given an array points where points[i] = [xi, yi] and an integer k, return the maximum value of yi + yj + |xi - xj| such that |xi - xj| <= k and i < j.

Constraints:
- 2 <= points.length <= 10^5
- -10^8 <= xi, yi <= 10^8
- xi < xj for all 1 <= i < j <= points.length
- 1 <= k <= 2 * 10^8

Example:
Input: points = [[1,3],[2,0],[3,10],[4,2],[5,3]], k = 1
Output: 4
"""
def findMaxValueOfEquation(points, k):
    from collections import deque
    res = float('-inf')
    dq = deque()
    for x, y in points:
        while dq and x - dq[0][1] > k:
            dq.popleft()
        if dq:
            res = max(res, y + x + dq[0][0])
        while dq and dq[-1][0] <= y - x:
            dq.pop()
        dq.append((y - x, x))
    return res

# Example usage:
points = [[1,3],[2,0],[3,10],[4,2],[5,3]]
k = 1
print(findMaxValueOfEquation(points, k))  # Output: 4
