"""
947. Most Stones Removed with Same Row or Column
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.
Return the largest possible number of stones that can be removed.

Constraints:
- 1 <= stones.length <= 1000
- 0 <= stones[i][j] < 10000

Example:
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
"""
from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]
        for x, y in stones:
            find((x, ~0))
            find((~0, y))
            parent[find((x, ~0))] = find((~0, y))
        return len(stones) - len({find((x, ~0)) for x, y in stones} | {find((~0, y)) for x, y in stones})

# Example usage
if __name__ == "__main__":
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    print(Solution().removeStones(stones))  # Output: 5
