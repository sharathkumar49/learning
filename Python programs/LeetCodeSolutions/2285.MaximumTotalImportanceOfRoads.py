"""
LeetCode 2285. Maximum Total Importance of Roads

Given n and roads, return the maximum total importance.

Example:
Input: n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
Output: 43

Constraints:
- 2 <= n <= 10^5
- 1 <= roads.length <= 10^5
"""

def maximumImportance(n, roads):
    degree = [0]*n
    for u, v in roads:
        degree[u] += 1
        degree[v] += 1
    degree.sort()
    res = 0
    for i, d in enumerate(degree):
        res += (i+1)*d
    return res

# Example usage:
# print(maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))  # Output: 43
