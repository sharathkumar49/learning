"""
351. Android Unlock Patterns

Given an Android 3x3 key lock screen and two integers m and n, return the number of possible unlock patterns of the Android lock screen, where the length of each pattern is between m and n inclusive.

Constraints:
- 1 <= m, n <= 9
- 1 <= m <= n <= 9
"""
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = [[0]*10 for _ in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5
        visited = [False]*10
        def dfs(cur, remain):
            if remain < 0:
                return 0
            if remain == 0:
                return 1
            visited[cur] = True
            res = 0
            for i in range(1, 10):
                if not visited[i] and (skip[cur][i] == 0 or visited[skip[cur][i]]):
                    res += dfs(i, remain-1)
            visited[cur] = False
            return res
        res = 0
        for l in range(m, n+1):
            res += dfs(1, l-1) * 4
            res += dfs(2, l-1) * 4
            res += dfs(5, l-1)
        return res

# Example usage:
m, n = 1, 1
print(Solution().numberOfPatterns(m, n))  # Output: 9
