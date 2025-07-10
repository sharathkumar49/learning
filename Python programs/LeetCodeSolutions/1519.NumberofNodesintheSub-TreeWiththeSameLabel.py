"""
LeetCode 1519. Number of Nodes in the Sub-Tree With the Same Label

Given a tree (an undirected graph) with n nodes labeled from 0 to n-1 and a string labels, return an array of the number of nodes in the subtree of each node with the same label as the node.

Constraints:
- 1 <= n <= 10^5
- labels.length == n
- labels is lowercase English letters.

Example:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
Output: [2,1,1,1,1,1,1]
"""
def countSubTrees(n, edges, labels):
    from collections import defaultdict
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    res = [0] * n
    def dfs(node, parent):
        count = [0] * 26
        idx = ord(labels[node]) - ord('a')
        count[idx] = 1
        for nei in tree[node]:
            if nei != parent:
                child = dfs(nei, node)
                for i in range(26):
                    count[i] += child[i]
        res[node] = count[idx]
        return count
    dfs(0, -1)
    return res

# Example usage:
n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
labels = "abaedcd"
print(countSubTrees(n, edges, labels))  # Output: [2,1,1,1,1,1,1]
