"""
LeetCode 1361. Validate Binary Tree Nodes

Given n nodes labeled from 0 to n-1 and two arrays leftChild and rightChild, return true if and only if all the given nodes form exactly one valid binary tree.

Constraints:
- 1 <= n <= 2 * 10^4
- leftChild.length == rightChild.length == n
- -1 <= leftChild[i], rightChild[i] < n

Example:
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: True
"""
def validateBinaryTreeNodes(n, leftChild, rightChild):
    parent = [0]*n
    for i in range(n):
        for c in (leftChild[i], rightChild[i]):
            if c != -1:
                if parent[c]:
                    return False
                parent[c] = 1
    root = parent.count(0)
    if root != 1:
        return False
    seen = set()
    def dfs(i):
        if i == -1 or i in seen:
            return
        seen.add(i)
        dfs(leftChild[i])
        dfs(rightChild[i])
    dfs(parent.index(0))
    return len(seen) == n

# Example usage:
n = 4
leftChild = [1,-1,3,-1]
rightChild = [2,-1,-1,-1]
print(validateBinaryTreeNodes(n, leftChild, rightChild))  # Output: True
