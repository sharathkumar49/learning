"""
LeetCode 1993. Operations on Tree

Design a tree with lock/unlock/upgrade operations.

Example:
Input: OperationsOnTree([2,2,-1,2,2], ["lock","unlock","upgrade"], [[2,2],[2,2],[2,2]])
Output: [None, None, None]

Constraints:
- n == parent.length
- 1 <= n <= 2000
- parent[0] == -1
- 0 <= parent[i] < n for i > 0
"""

class LockingTree:
    def __init__(self, parent):
        self.parent = parent
        self.locked = [0]*len(parent)
        self.children = [[] for _ in parent]
        for i, p in enumerate(parent):
            if p != -1:
                self.children[p].append(i)
    def lock(self, num, user):
        if self.locked[num]: return False
        self.locked[num] = user
        return True
    def unlock(self, num, user):
        if self.locked[num] != user: return False
        self.locked[num] = 0
        return True
    def upgrade(self, num, user):
        if self.locked[num]: return False
        p = self.parent[num]
        while p != -1:
            if self.locked[p]: return False
            p = self.parent[p]
        found = False
        def dfs(u):
            nonlocal found
            if self.locked[u]:
                self.locked[u] = 0
                found = True
            for v in self.children[u]:
                dfs(v)
        dfs(num)
        if not found: return False
        self.locked[num] = user
        return True

# Example usage:
# tree = LockingTree([2,2,-1,2,2])
# print(tree.lock(2,2))
