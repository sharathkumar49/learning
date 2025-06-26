# Microsoft: Find the Number of Connected Components in an Undirected Graph
# Given n nodes labeled from 0 to n-1 and a list of undirected edges, return the number of connected components.

def count_components(n, edges):
    parent = [i for i in range(n)]
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, b in edges:
        pa, pb = find(a), find(b)
        if pa != pb:
            parent[pa] = pb
    return len(set(find(i) for i in range(n)))

if __name__ == "__main__":
    n1 = 5
    edges1 = [[0,1],[1,2],[3,4]]
    print(count_components(n1, edges1))  # Output: 2
    n2 = 5
    edges2 = [[0,1],[1,2],[2,3],[3,4]]
    print(count_components(n2, edges2))  # Output: 1
