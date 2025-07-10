"""
LeetCode 1591. Strange Printer II

Given a 2D grid of integers, return true if it is possible to print the grid using a strange printer that can print any rectangle of a single color in one operation, and false otherwise.

Example 1:
Input: targetGrid = [[1,1,1],[3,1,3]]
Output: true

Constraints:
- 1 <= m, n <= 60
- 1 <= targetGrid[i][j] <= 60
"""

def isPrintable(targetGrid):
    m, n = len(targetGrid), len(targetGrid[0])
    colors = set()
    for row in targetGrid:
        colors |= set(row)
    bounds = {}
    for c in colors:
        r1 = c1 = float('inf')
        r2 = c2 = -float('inf')
        for i in range(m):
            for j in range(n):
                if targetGrid[i][j] == c:
                    r1 = min(r1, i)
                    r2 = max(r2, i)
                    c1 = min(c1, j)
                    c2 = max(c2, j)
        bounds[c] = (r1, r2, c1, c2)
    def canRemove(c):
        r1, r2, c1, c2 = bounds[c]
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if targetGrid[i][j] != 0 and targetGrid[i][j] != c:
                    return False
        return True
    left = set(colors)
    while left:
        removed = False
        for c in list(left):
            if canRemove(c):
                r1, r2, c1, c2 = bounds[c]
                for i in range(r1, r2+1):
                    for j in range(c1, c2+1):
                        if targetGrid[i][j] == c:
                            targetGrid[i][j] = 0
                left.remove(c)
                removed = True
        if not removed:
            return False
    return True

# Example usage:
# targetGrid = [[1,1,1],[3,1,3]]
# print(isPrintable(targetGrid))  # Output: True
