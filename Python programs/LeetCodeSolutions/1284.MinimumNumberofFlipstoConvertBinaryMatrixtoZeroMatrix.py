"""
LeetCode 1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix

Given a m x n binary matrix, in one step you can choose any cell and flip it and its four neighbors. Return the minimum number of steps to convert the matrix to a zero matrix, or -1 if impossible.

Constraints:
- 1 <= m <= 3
- 1 <= n <= 3

Example:
Input: mat = [[0,0],[0,1]]
Output: 3
"""
def minFlips(mat):
    from collections import deque
    m, n = len(mat), len(mat[0])
    start = sum(mat[i][j] << (i*n+j) for i in range(m) for j in range(n))
    queue = deque([(start, 0)])
    seen = {start}
    dirs = [(0,0),(0,1),(0,-1),(1,0),(-1,0)]
    while queue:
        state, steps = queue.popleft()
        if state == 0:
            return steps
        for i in range(m):
            for j in range(n):
                nxt = state
                for dx, dy in dirs:
                    ni, nj = i+dx, j+dy
                    if 0<=ni<m and 0<=nj<n:
                        nxt ^= 1 << (ni*n+nj)
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, steps+1))
    return -1

# Example usage:
mat = [[0,0],[0,1]]
print(minFlips(mat))  # Output: 3
