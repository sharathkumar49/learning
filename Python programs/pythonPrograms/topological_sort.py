# Topological sort (for DAG)
from collections import defaultdict, deque

def topological_sort(V, edges):
    graph = defaultdict(list)
    indegree = {i:0 for i in range(V)}
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    q = deque([u for u in indegree if indegree[u]==0])
    res = []
    while q:
        u = q.popleft()
        res.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    return res if len(res) == V else []

if __name__ == "__main__":
    V = int(input("Number of vertices: "))
    E = int(input("Number of edges: "))
    edges = [tuple(map(int, input().split())) for _ in range(E)]
    print("Topological order:", topological_sort(V, edges))
