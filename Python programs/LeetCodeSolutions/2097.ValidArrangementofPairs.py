"""
LeetCode 2097. Valid Arrangement of Pairs

Given pairs of integers, return a valid arrangement of pairs such that for every pair, the second element of the previous pair is the first element of the next pair.

Example:
Input: pairs = [[5,1],[4,5],[1,4]]
Output: [[4,5],[5,1],[1,4]]

Constraints:
- 1 <= pairs.length <= 10^5
- 0 <= pairs[i][0], pairs[i][1] <= 10^5
"""

def validArrangement(pairs):
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v in pairs:
        graph[u].append(v)
    res = []
    def dfs(u):
        while graph[u]:
            dfs(graph[u].pop())
        res.append(u)
    dfs(pairs[0][0])
    return [[res[i], res[i-1]] for i in range(len(res)-1, 0, -1)]

# Example usage:
# print(validArrangement([[5,1],[4,5],[1,4]]))  # Output: [[4,5],[5,1],[1,4]]
