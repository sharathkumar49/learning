# Dijkstra's shortest path algorithm
import heapq

def dijkstra(graph, start):
    heap = [(0, start)]
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    while heap:
        d, node = heapq.heappop(heap)
        for neighbor, weight in graph[node]:
            if dist[neighbor] > d + weight:
                dist[neighbor] = d + weight
                heapq.heappush(heap, (dist[neighbor], neighbor))
    return dist

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    print(dijkstra(graph, 'A'))
