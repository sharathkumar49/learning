"""
1203. Sort Items by Groups Respecting Dependencies

Given n items, some belonging to groups, and a list of dependencies, return a sorted list of items respecting group and item dependencies. If impossible, return an empty list.

Constraints:
- 1 <= n <= 3 * 10^4
- m == group.length
- -1 <= group[i] < m
- 0 <= beforeItems.length == n
- 0 <= beforeItems[i].length < n

Example:
Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]

"""
def sortItems(n, m, group, beforeItems):
    from collections import defaultdict, deque
    for i in range(n):
        if group[i] == -1:
            group[i] = m
            m += 1
    item_graph = defaultdict(list)
    item_indegree = [0]*n
    group_graph = defaultdict(list)
    group_indegree = [0]*m
    for i in range(n):
        for j in beforeItems[i]:
            item_graph[j].append(i)
            item_indegree[i] += 1
            if group[i] != group[j]:
                group_graph[group[j]].append(group[i])
                group_indegree[group[i]] += 1
    def topo(graph, indegree, nodes):
        q = deque([i for i in nodes if indegree[i] == 0])
        res = []
        while q:
            u = q.popleft()
            res.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return res if len(res) == len(nodes) else []
    group_items = defaultdict(list)
    for i in range(n):
        group_items[group[i]].append(i)
    group_order = topo(group_graph, group_indegree, list(range(m)))
    if not group_order:
        return []
    res = []
    for g in group_order:
        order = topo(item_graph, item_indegree, group_items[g])
        if not order:
            return []
        res += order
    return res

# Example usage
if __name__ == "__main__":
    n = 8
    m = 2
    group = [-1,-1,1,0,0,1,0,-1]
    beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
    print(sortItems(n, m, group, beforeItems))  # Output: [6,3,4,1,5,2,0,7]
