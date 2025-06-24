"""
1135. Connecting Cities With Minimum Cost

There are n cities and connections[i] = [city1, city2, cost]. Return the minimum cost to connect all cities, or -1 if impossible.

Constraints:
- 1 <= n <= 10000
- 1 <= connections.length <= 10000
- 1 <= cost <= 10^5

Example:
Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6

"""
def minimumCost(n, connections):
    parent = list(range(n+1))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    connections.sort(key=lambda x: x[2])
    res = 0
    count = 0
    for u, v, cost in connections:
        pu, pv = find(u), find(v)
        if pu != pv:
            parent[pu] = pv
            res += cost
            count += 1
    return res if count == n-1 else -1

# Example usage
if __name__ == "__main__":
    print(minimumCost(3, [[1,2,5],[1,3,6],[2,3,1]]))  # Output: 6
