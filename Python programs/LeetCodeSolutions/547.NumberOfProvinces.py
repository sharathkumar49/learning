"""
547. Number of Provinces

There are n cities. Some of them are connected, while some are not. A province is a group of directly or indirectly connected cities. Return the number of provinces.

Constraints:
- 1 <= n <= 200
- isConnected.length == n
- isConnected[i].length == n
- isConnected[i][j] is 1 or 0

Example:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
"""

class Solution:
    def findCircleNum(self, isConnected: list) -> int:
        n = len(isConnected)
        visited = [False] * n
        def dfs(i):
            for j in range(n):
                if isConnected[i][j] and not visited[j]:
                    visited[j] = True
                    dfs(j)
        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count

# Example usage:
sol = Solution()
print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))  # Output: 2
