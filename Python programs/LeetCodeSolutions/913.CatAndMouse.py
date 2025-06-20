"""
913. Cat and Mouse
https://leetcode.com/problems/cat-and-mouse/

A game is played on a directed graph where two players, Mouse and Cat, move alternately. The Mouse starts at node 1 and the Cat starts at node 2. The Cat cannot move to node 0. The game ends when:
- The Mouse reaches node 0 (Mouse wins).
- The Cat catches the Mouse (Cat and Mouse are on the same node, Cat wins).
- The game is a draw if it repeats forever.
Given a graph represented as an adjacency list, return 0 if the Mouse wins, 1 if the Cat wins, or 2 if the game is a draw.

Constraints:
- 3 <= graph.length <= 50
- 1 <= graph[i].length < graph.length
- 0 <= graph[i][j] < graph.length
- graph[i][j] != i

Example:
Input: graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
Output: 0
"""
from typing import List

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        dp = [[[None]*3 for _ in range(n)] for _ in range(n)]
        def helper(m, c, t):
            if t == 2*n: return 2
            if m == 0: return 0
            if m == c: return 1
            if dp[m][c][t%2] is not None:
                return dp[m][c][t%2]
            if t % 2 == 0:
                # Mouse's turn
                for nei in graph[m]:
                    if helper(nei, c, t+1) == 0:
                        dp[m][c][t%2] = 0
                        return 0
                for nei in graph[m]:
                    if helper(nei, c, t+1) == 2:
                        dp[m][c][t%2] = 2
                        return 2
                dp[m][c][t%2] = 1
                return 1
            else:
                # Cat's turn
                for nei in graph[c]:
                    if nei == 0:
                        continue
                    if helper(m, nei, t+1) == 1:
                        dp[m][c][t%2] = 1
                        return 1
                for nei in graph[c]:
                    if nei == 0:
                        continue
                    if helper(m, nei, t+1) == 2:
                        dp[m][c][t%2] = 2
                        return 2
                dp[m][c][t%2] = 0
                return 0
        return helper(1, 2, 0)

# Example usage
if __name__ == "__main__":
    graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
    print(Solution().catMouseGame(graph))  # Output: 0
