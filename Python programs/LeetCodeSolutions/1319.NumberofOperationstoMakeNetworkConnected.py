"""
LeetCode 1319. Number of Operations to Make Network Connected

There are n computers and connections. You can extract a cable between two directly connected computers and place it between any two computers to make them directly connected. Return the minimum number of operations to connect all computers, or -1 if impossible.

Constraints:
- 1 <= n <= 10^5
- 1 <= connections.length <= min(n*(n-1)/2, 10^5)
- connections[i].length == 2
- 0 <= connections[i][j] < n

Example:
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
"""
def makeConnected(n, connections):
    if len(connections) < n-1:
        return -1
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, b in connections:
        parent[find(a)] = find(b)
    return len(set(find(x) for x in range(n))) - 1

# Example usage:
n = 4
connections = [[0,1],[0,2],[1,2]]
print(makeConnected(n, connections))  # Output: 1
