# Program: Implement a Queue for Topological Sort (Kahn's Algorithm)
# Problem: Use a queue to perform topological sorting of a directed acyclic graph (DAG).
from collections import deque, defaultdict

class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self, val):
        self.buffer.appendleft(val)
    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)

def topological_sort_kahn(V, edges):
    graph = defaultdict(list)
    indegree = [0]*V
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    q = Queue()
    for i in range(V):
        if indegree[i] == 0:
            q.enqueue(i)
    topo = []
    while not q.is_empty():
        u = q.dequeue()
        topo.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.enqueue(v)
    return topo if len(topo) == V else []

if __name__ == '__main__':
    V = 6
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    print(topological_sort_kahn(V, edges))
