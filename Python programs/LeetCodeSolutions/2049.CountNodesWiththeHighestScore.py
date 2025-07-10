"""
LeetCode 2049. Count Nodes With the Highest Score

Given a binary tree, return the number of nodes with the highest score, where the score of a node is the product of the sizes of the subtrees after removing that node.

Example:
Input: parents = [-1,2,0,2,0]
Output: 3

Constraints:
- n == parents.length
- 2 <= n <= 10^5
- 0 <= parents[i] <= n - 1
"""

def countHighestScoreNodes(parents):
    from collections import defaultdict
    n = len(parents)
    tree = defaultdict(list)
    for i, p in enumerate(parents):
        if p != -1:
            tree[p].append(i)
    res = [0] * n
    def dfs(u):
        score = 1
        size = n - 1
        for v in tree[u]:
            t = dfs(v)
            score *= t
            size -= t
        if u != 0:
            score *= size
        res[u] = score
        return n - size
    dfs(0)
    max_score = max(res)
    return res.count(max_score)

# Example usage:
# print(countHighestScoreNodes([-1,2,0,2,0]))  # Output: 3
