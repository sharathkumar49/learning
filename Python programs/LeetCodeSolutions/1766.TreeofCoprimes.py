"""
LeetCode 1766. Tree of Coprimes

Given a tree and an array nums, return an array where the ith element is the closest ancestor of node i with a coprime value.

Example 1:
Input: nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]
Output: [-1,0,0,1]

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 50
- edges.length == nums.length - 1
"""

def getCoprimes(nums, edges):
    from math import gcd
    from collections import defaultdict
    n = len(nums)
    tree = [[] for _ in range(n)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    res = [-1]*n
    stack = [[] for _ in range(51)]
    def dfs(u, p, depth):
        max_depth, ancestor = -1, -1
        for v in range(1, 51):
            if stack[v] and gcd(nums[u], v) == 1:
                if stack[v][-1][1] > max_depth:
                    max_depth = stack[v][-1][1]
                    ancestor = stack[v][-1][0]
        res[u] = ancestor
        stack[nums[u]].append((u, depth))
        for v in tree[u]:
            if v != p:
                dfs(v, u, depth+1)
        stack[nums[u]].pop()
    dfs(0, -1, 0)
    return res

# Example usage:
# nums = [2,3,3,2]
# edges = [[0,1],[1,2],[1,3]]
# print(getCoprimes(nums, edges))  # Output: [-1,0,0,1]
