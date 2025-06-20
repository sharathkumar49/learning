"""
834. Sum of Distances in Tree

Given a tree with n nodes labeled from 0 to n-1 and an array edges, return an array answer where answer[i] is the sum of the distances between the i-th node and all other nodes.

Example 1:
Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]

Constraints:
- 1 <= n <= 3 * 10^4
- edges.length == n - 1
- 0 <= edges[i][j] < n
- The given input is a tree.
"""
def sumOfDistancesInTree(n, edges):
    from collections import defaultdict
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    res = [0] * n
    count = [1] * n
    def dfs(node, parent):
        for child in tree[node]:
            if child != parent:
                dfs(child, node)
                count[node] += count[child]
                res[node] += res[child] + count[child]
    def dfs2(node, parent):
        for child in tree[node]:
            if child != parent:
                res[child] = res[node] - count[child] + (n - count[child])
                dfs2(child, node)
    dfs(0, -1)
    dfs2(0, -1)
    return res

# Example usage:
print(sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))  # Output: [8,12,6,10,10,10]
