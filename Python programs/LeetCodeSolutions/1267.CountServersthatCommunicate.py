"""
LeetCode 1267. Count Servers that Communicate

You are given a m x n binary matrix grid where 1 represents a server and 0 represents an empty cell. Two servers communicate if they are in the same row or column. Return the number of servers that can communicate with at least one other server.

Constraints:
- 1 <= m <= 250
- 1 <= n <= 250
- grid[i][j] is either 0 or 1

Example:
Input: grid = [[1,0],[0,1]]
Output: 0

"""
def countServers(grid):
    m, n = len(grid), len(grid[0])
    row = [0]*m
    col = [0]*n
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                row[i] += 1
                col[j] += 1
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] and (row[i] > 1 or col[j] > 1):
                res += 1
    return res

# Example usage:
grid = [[1,0],[0,1]]
print(countServers(grid))  # Output: 0
