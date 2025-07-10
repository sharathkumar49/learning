"""
LeetCode 1820. Maximum Number of Accepted Invitations

Given a grid where grid[i][j] = 1 means the ith boy can invite the jth girl, return the maximum number of invitations that can be accepted.

Example 1:
Input: grid = [[1,1,1],[1,0,1],[0,0,1]]
Output: 3

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- grid[i][j] is 0 or 1
"""

def maximumInvitations(grid):
    m, n = len(grid), len(grid[0])
    match = [-1]*n
    def bpm(u, vis):
        for v in range(n):
            if grid[u][v] and not vis[v]:
                vis[v] = True
                if match[v] == -1 or bpm(match[v], vis):
                    match[v] = u
                    return True
        return False
    res = 0
    for u in range(m):
        vis = [False]*n
        if bpm(u, vis):
            res += 1
    return res

# Example usage:
# grid = [[1,1,1],[1,0,1],[0,0,1]]
# print(maximumInvitations(grid))  # Output: 3
