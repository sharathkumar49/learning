"""
LeetCode 1916. Count Ways to Build Rooms in an Ant Colony

Given an array prevRoom, return the number of ways to build all the rooms modulo 10^9+7.

Example:
Input: prevRoom = [-1,0,1]
Output: 1

Constraints:
- 2 <= prevRoom.length <= 10^5
- prevRoom[0] == -1
- 0 <= prevRoom[i] < i for all 1 <= i < n
"""

MOD = 10**9+7

def waysToBuildRooms(prevRoom):
    from math import comb
    import sys
    sys.setrecursionlimit(1 << 20)
    n = len(prevRoom)
    tree = [[] for _ in range(n)]
    for i in range(1, n):
        tree[prevRoom[i]].append(i)
    fact = [1]*(n+1)
    for i in range(1, n+1):
        fact[i] = fact[i-1]*i%MOD
    inv = [1]*(n+1)
    inv[n] = pow(fact[n], MOD-2, MOD)
    for i in range(n-1, -1, -1):
        inv[i] = inv[i+1]*(i+1)%MOD
    def dfs(u):
        res, sz = 1, 0
        for v in tree[u]:
            r, s = dfs(v)
            res = res*r*comb(sz+s, s)%MOD
            sz += s
        return res, sz+1
    return dfs(0)[0]

# Example usage:
# print(waysToBuildRooms([-1,0,1]))  # Output: 1
