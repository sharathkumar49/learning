# Microsoft: Find All Paths from Source to Target in a Directed Acyclic Graph
# Given a DAG, return all possible paths from node 0 to node n-1.

def all_paths_source_target(graph):
    res = []
    def dfs(node, path):
        if node == len(graph) - 1:
            res.append(path[:])
            return
        for nei in graph[node]:
            dfs(nei, path + [nei])
    dfs(0, [0])
    return res

if __name__ == "__main__":
    graph1 = [[1,2],[3],[3],[]]
    print(all_paths_source_target(graph1))  # Output: [[0,1,3],[0,2,3]]
    graph2 = [[4,3,1],[3,2,4],[3],[4],[]]
    print(all_paths_source_target(graph2))
