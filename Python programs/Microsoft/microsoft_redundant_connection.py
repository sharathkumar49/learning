# Microsoft: Find the Redundant Connection
# In a tree with n nodes, one extra edge is added. Find the edge that can be removed so that the resulting graph is a tree.

def find_redundant_connection(edges):
    parent = [i for i in range(len(edges)+1)]
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, b in edges:
        pa, pb = find(a), find(b)
        if pa == pb:
            return [a, b]
        parent[pa] = pb
    return []

if __name__ == "__main__":
    edges1 = [[1,2],[1,3],[2,3]]
    print(find_redundant_connection(edges1))  # Output: [2,3]
    edges2 = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    print(find_redundant_connection(edges2))  # Output: [1,4]
