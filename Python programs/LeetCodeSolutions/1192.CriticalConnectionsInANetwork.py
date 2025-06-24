"""
1192. Critical Connections in a Network

Given a network of n servers and a list of connections, return all critical connections (bridges) in the network.

Constraints:
- 1 <= n <= 10^5
- connections.length == n - 1
- 0 <= connections[i][j] < n

Example:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]

"""
def criticalConnections(n, connections):
    graph = [[] for _ in range(n)]
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
    res = []
    low = [0]*n
    disc = [0]*n
    time = [1]
    def dfs(u, parent):
        disc[u] = low[u] = time[0]
        time[0] += 1
        for v in graph[u]:
            if not disc[v]:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    res.append([u, v])
            elif v != parent:
                low[u] = min(low[u], disc[v])
    dfs(0, -1)
    return res

# Example usage
if __name__ == "__main__":
    print(criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))  # Output: [[1,3]]
