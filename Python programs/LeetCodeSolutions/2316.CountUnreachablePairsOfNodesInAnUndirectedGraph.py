"""
LeetCode 2316. Count Unreachable Pairs of Nodes in an Undirected Graph

Given n and edges, return the number of pairs of nodes that are unreachable from each other.

Example:
Input: n = 3, edges = [[0,1],[0,2]]
Output: 0

Constraints:
- 1 <= n <= 10^5
- 0 <= edges.length <= 2 * 10^5
"""

def countPairs(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in edges:
        parent[find(u)] = find(v)
    from collections import Counter
    sizes = Counter(find(i) for i in range(n)).values()
    total = n * (n-1) // 2
    for size in sizes:
        total -= size * (size-1) // 2
    return total

# Example usage:
# print(countPairs(3, [[0,1],[0,2]]))  # Output: 0
