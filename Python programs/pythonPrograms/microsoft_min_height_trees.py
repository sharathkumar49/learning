# Microsoft: Find the Minimum Height Trees
# Given a tree with n nodes labeled from 0 to n-1, return all the root labels of Minimum Height Trees.
from collections import deque

def find_min_height_trees(n, edges):
    if n == 1:
        return [0]
    graph = [set() for _ in range(n)]
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)
    leaves = [i for i in range(n) if len(graph[i]) == 1]
    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
        leaves = new_leaves
    return leaves

if __name__ == "__main__":
    n1 = 4
    edges1 = [[1,0],[1,2],[1,3]]
    print(find_min_height_trees(n1, edges1))  # Output: [1]
    n2 = 6
    edges2 = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    print(find_min_height_trees(n2, edges2))  # Output: [3,4]
