# Microsoft: Clone Graph (DFS/BFS)
# Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node):
    if not node:
        return None
    old_to_new = {}
    def dfs(n):
        if n in old_to_new:
            return old_to_new[n]
        copy = Node(n.val)
        old_to_new[n] = copy
        for nei in n.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy
    return dfs(node)

# Example usage (for testing):
if __name__ == "__main__":
    # Build a simple graph: 1 -- 2
    n1 = Node(1)
    n2 = Node(2)
    n1.neighbors.append(n2)
    n2.neighbors.append(n1)
    clone = clone_graph(n1)
    print(clone.val)  # 1
    print([n.val for n in clone.neighbors])  # [2]
    print([n.val for n in clone.neighbors[0].neighbors])  # [1]
