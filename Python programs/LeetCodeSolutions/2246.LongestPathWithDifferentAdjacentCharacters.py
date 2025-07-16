"""
LeetCode 2246. Longest Path With Different Adjacent Characters

Given parent and s, return the length of the longest path with different adjacent characters.

Example:
Input: parent = [-1,0,0,1,1,2], s = "abacbe"
Output: 3

Constraints:
- 1 <= parent.length == s.length <= 10^5
- parent[0] == -1
- s consists of lowercase English letters
"""

def longestPath(parent, s):
    from collections import defaultdict
    tree = defaultdict(list)
    for i in range(1, len(parent)):
        tree[parent[i]].append(i)
    res = [0]
    def dfs(u):
        max1 = max2 = 0
        for v in tree[u]:
            l = dfs(v)
            if s[v] != s[u]:
                if l > max1:
                    max2 = max1
                    max1 = l
                elif l > max2:
                    max2 = l
        res[0] = max(res[0], max1+max2+1)
        return max1+1
    dfs(0)
    return res[0]

# Example usage:
# print(longestPath([-1,0,0,1,1,2], "abacbe"))  # Output: 3
