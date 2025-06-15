# Program: Implement a Queue for Shortest Path in Unweighted Graph (BFS)
# Problem: Find the shortest path from source to all vertices in an unweighted graph using BFS (queue).
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

def shortest_path_unweighted(V, edges, src):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    dist = [float('inf')]*V
    dist[src] = 0
    q = Queue()
    q.enqueue(src)
    while not q.is_empty():
        u = q.dequeue()
        for v in graph[u]:
            if dist[v] == float('inf'):
                dist[v] = dist[u] + 1
                q.enqueue(v)
    return dist

if __name__ == '__main__':
    V = 6
    edges = [(0,1),(0,2),(1,3),(2,3),(3,4),(4,5)]
    print(shortest_path_unweighted(V, edges, 0))
