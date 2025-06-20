"""
863. All Nodes Distance K in Binary Tree

Given the root of a binary tree, a target node, and an integer k, return all the values of the nodes that have a distance k from the target node.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]

Constraints:
- The number of nodes in the tree is in the range [1, 500].
- 0 <= Node.val <= 500
- All the values of the nodes are unique.
- target is a node in the tree.
- 0 <= k <= 1000
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def distanceK(root, target, k):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    def build(node, parent):
        if node:
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            build(node.left, node)
            build(node.right, node)
    build(root, None)
    queue = deque([(target.val, 0)])
    seen = {target.val}
    res = []
    while queue:
        node, dist = queue.popleft()
        if dist == k:
            res.append(node)
        elif dist < k:
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, dist+1))
    return res

# Example usage:
# Helper function to build a tree and find target node
# ...omitted for brevity...
