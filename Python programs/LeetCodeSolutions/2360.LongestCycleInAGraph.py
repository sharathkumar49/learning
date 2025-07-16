"""
LeetCode 2360. Longest Cycle in a Graph

Given edges, return the length of the longest cycle in the graph.

Example:
Input: edges = [3,3,4,2,3]
Output: 3

Constraints:
- 1 <= edges.length <= 10^5
"""

def longestCycle(edges):
    n = len(edges)
    vis = [-1]*n
    res = -1
    for i in range(n):
        if vis[i] != -1:
            continue
        stack = []
        curr = i
        step = 0
        while curr != -1 and vis[curr] == -1:
            vis[curr] = step
            stack.append(curr)
            curr = edges[curr]
            step += 1
        if curr != -1 and curr in stack:
            res = max(res, step - vis[curr])
    return res

# Example usage:
# print(longestCycle([3,3,4,2,3]))  # Output: 3
