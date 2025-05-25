# Amazon: Find the maximum path sum in a binary tree
def max_path_sum(root):
    max_sum = float('-inf')
    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)
        max_sum = max(max_sum, node.val + left + right)
        return node.val + max(left, right)
    dfs(root)
    return max_sum

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

if __name__ == "__main__":
    a = Node(1); b = Node(2); c = Node(3)
    a.left = b; a.right = c
    print("Max path sum:", max_path_sum(a))
