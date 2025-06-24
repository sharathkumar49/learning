"""
1168. Optimize Water Distribution in a Village

There are n houses in a village. Some houses have wells, and there are pipes between houses. Each well and pipe has a cost. Return the minimum total cost to supply water to all houses.

Constraints:
- 1 <= n <= 10000
- wells.length == n
- 0 <= pipes.length <= min(20000, n * (n - 1) / 2)
- 1 <= wells[i], cost for pipes[i][2] <= 10^5

Example:
Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
Output: 3

"""
def minCostToSupplyWater(n, wells, pipes):
    parent = list(range(n+1))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    edges = [[w, 0, i+1] for i, w in enumerate(wells)] + [[c, u, v] for u, v, c in pipes]
    edges.sort()
    res = 0
    for c, u, v in edges:
        pu, pv = find(u), find(v)
        if pu != pv:
            parent[pu] = pv
            res += c
    return res

# Example usage
if __name__ == "__main__":
    print(minCostToSupplyWater(3, [1,2,2], [[1,2,1],[2,3,1]]))  # Output: 3
