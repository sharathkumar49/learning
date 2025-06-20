"""
261. Graph Valid Tree
https://leetcode.com/problems/graph-valid-tree/

Given n nodes labeled from 0 to n - 1 and a list of undirected edges, write a function to check whether these edges make up a valid tree.

Constraints:
- 1 <= n <= 2000
- 0 <= edges.length <= n * (n - 1) / 2
- 0 <= ai, bi < n
- ai != bi
- There are no repeated edges.

Example 1:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
"""
def validTree(n, edges):
    if len(edges) != n - 1:
        return False
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, b in edges:
        pa, pb = find(a), find(b)
        if pa == pb:
            return False
        parent[pa] = pb
    return True

# Example usage:
if __name__ == "__main__":
    print(validTree(5, [[0,1],[0,2],[0,3],[1,4]]))  # Output: True
    print(validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))  # Output: False
