"""
LeetCode 1627. Graph Connectivity With Threshold

Given n nodes and a threshold, return the number of connected components in the graph where an edge exists between nodes i and j if gcd(i, j) > threshold.

Example 1:
Input: n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]
Output: [false,false,true]

Constraints:
- 1 <= n <= 10^4
- 0 <= threshold <= n
- 1 <= queries.length <= 10^5
- queries[i].length == 2
"""

def areConnected(n, threshold, queries):
    parent = list(range(n+1))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i in range(threshold+1, n+1):
        for j in range(2*i, n+1, i):
            parent[find(j)] = find(i)
    return [find(x)==find(y) for x,y in queries]

# Example usage:
# n = 6
# threshold = 2
# queries = [[1,4],[2,5],[3,6]]
# print(areConnected(n, threshold, queries))  # Output: [False, False, True]
