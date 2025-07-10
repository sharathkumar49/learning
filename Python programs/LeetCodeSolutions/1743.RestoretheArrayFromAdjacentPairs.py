"""
LeetCode 1743. Restore the Array From Adjacent Pairs

Given an array of adjacent pairs, restore the original array.

Example 1:
Input: adjacentPairs = [[2,1],[3,4],[3,2]]
Output: [4,3,2,1]

Constraints:
- 2 <= adjacentPairs.length <= 10^5
- adjacentPairs[i].length == 2
- -10^5 <= each integer <= 10^5
"""

def restoreArray(adjacentPairs):
    from collections import defaultdict
    adj = defaultdict(list)
    for a, b in adjacentPairs:
        adj[a].append(b)
        adj[b].append(a)
    for k, v in adj.items():
        if len(v) == 1:
            start = k
            break
    res = [start]
    while len(res) < len(adj):
        for nei in adj[res[-1]]:
            if len(res) == 1 or nei != res[-2]:
                res.append(nei)
                break
    return res

# Example usage:
# adjacentPairs = [[2,1],[3,4],[3,2]]
# print(restoreArray(adjacentPairs))  # Output: [4,3,2,1]
