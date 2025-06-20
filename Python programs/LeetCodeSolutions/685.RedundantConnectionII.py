"""
LeetCode 685. Redundant Connection II

In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) with in-degree 0, and every other node has in-degree 1. The given graph started as a rooted tree with n nodes (with distinct values from 1 to n), with one additional directed edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.

Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
Output: [4,1]

Constraints:
- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2
- 1 <= ai, bi <= n
"""
from typing import List

def findRedundantDirectedConnection(edges: List[List[int]]) -> List[int]:
    n = len(edges)
    parent = [0] * (n + 1)
    cand1 = cand2 = None
    for u, v in edges:
        if parent[v] == 0:
            parent[v] = u
        else:
            cand1 = [parent[v], v]
            cand2 = [u, v]
            break
    def find(u, parents):
        while parents[u] != u:
            parents[u] = parents[parents[u]]
            u = parents[u]
        return u
    def union(edges, skip):
        parents = [i for i in range(n+1)]
        for u, v in edges:
            if [u, v] == skip:
                continue
            pu, pv = find(u, parents), find(v, parents)
            if pu == pv:
                return [u, v]
            parents[pv] = pu
        return None
    if not cand1:
        return union(edges, None)
    if not union(edges, cand2):
        return cand2
    return cand1

# Example usage
if __name__ == "__main__":
    print(findRedundantDirectedConnection([[1,2],[1,3],[2,3]]))  # Output: [2,3]
    print(findRedundantDirectedConnection([[1,2],[2,3],[3,4],[4,1],[1,5]]))  # Output: [4,1]
