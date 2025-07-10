"""
LeetCode 1982. Find Array From Adjacent Pairs

Given pairs of adjacent elements, return the original array.

Example:
Input: adjacentPairs = [[2,1],[3,4],[3,2]]
Output: [1,2,3,4]

Constraints:
- n == adjacentPairs.length + 1
- 2 <= n <= 10^5
- -10^5 <= nums[i] <= 10^5
"""

def restoreArray(adjacentPairs):
    from collections import defaultdict
    g = defaultdict(list)
    for a, b in adjacentPairs:
        g[a].append(b)
        g[b].append(a)
    for k, v in g.items():
        if len(v) == 1:
            start = k
            break
    res = [start]
    while len(res) < len(adjacentPairs) + 1:
        for nei in g[res[-1]]:
            if len(res) == 1 or nei != res[-2]:
                res.append(nei)
                break
    return res

# Example usage:
# print(restoreArray([[2,1],[3,4],[3,2]]))  # Output: [1,2,3,4]
