"""
LeetCode 1443. Minimum Time to Collect All Apples in a Tree

Given an undirected tree with n nodes and a boolean array hasApple, return the minimum time to collect all apples. Each edge takes 1 second to traverse.

Constraints:
- 1 <= n <= 10^5
- edges.length == n-1
- 0 <= ai, bi <= n-1
- hasApple.length == n

Example:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,True,True,False]
Output: 8
"""
def minTime(n, edges, hasApple):
    from collections import defaultdict
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    def dfs(node, parent):
        time = 0
        for child in tree[node]:
            if child != parent:
                t = dfs(child, node)
                if t > 0 or hasApple[child]:
                    time += t + 2
        return time
    return dfs(0, -1)

# Example usage:
n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]
print(minTime(n, edges, hasApple))  # Output: 8
