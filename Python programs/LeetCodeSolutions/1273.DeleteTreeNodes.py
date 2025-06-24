"""
LeetCode 1273. Delete Tree Nodes

A tree rooted at node 0 is given as a parent array and a value array. Deleting a node deletes all its children. Return the number of nodes remaining after deleting every subtree whose sum of values is zero.

Constraints:
- 1 <= nodes <= 10^4
- parent.length == nodes
- value.length == nodes
- parent[0] == -1
- -10^5 <= value[i] <= 10^5

Example:
Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,2,0,0,2,-2,-2]
Output: 2
"""
def deleteTreeNodes(nodes, parent, value):
    from collections import defaultdict
    tree = defaultdict(list)
    for i in range(1, nodes):
        tree[parent[i]].append(i)
    def dfs(u):
        total, count = value[u], 1
        for v in tree[u]:
            t, c = dfs(v)
            total += t
            count += c if t != 0 else 0
        return (total, 0) if total == 0 else (total, count)
    return dfs(0)[1]

# Example usage:
nodes = 7
parent = [-1,0,0,1,2,2,2]
value = [1,2,0,0,2,-2,-2]
print(deleteTreeNodes(nodes, parent, value))  # Output: 2
