"""
1197. Minimum Knight Moves

Given two integers x and y, return the minimum number of steps required for a knight to reach (x, y) from (0, 0) on an infinite chessboard.

Constraints:
- -300 <= x, y <= 300

Example:
Input: x = 2, y = 1
Output: 1

"""
def minKnightMoves(x, y):
    from collections import deque
    x, y = abs(x), abs(y)
    visited = set()
    q = deque([(0, 0, 0)])
    while q:
        i, j, d = q.popleft()
        if (i, j) == (x, y):
            return d
        for di, dj in [(-2,-1),(-1,-2),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)]:
            ni, nj = abs(i+di), abs(j+dj)
            if (ni, nj) not in visited and ni >= 0 and nj >= 0:
                visited.add((ni, nj))
                q.append((ni, nj, d+1))
    return -1

# Example usage
if __name__ == "__main__":
    print(minKnightMoves(2, 1))  # Output: 1
