"""
536. Construct Binary Tree from String

You need to construct a binary tree from a string consisting of parenthesis and integers.

Constraints:
- 1 <= s.length <= 10^4
- s consists of digits, '(', ')', and '-'.

Example:
Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not s:
            return None
        def parse(i):
            j = i
            while j < len(s) and (s[j] == '-' or s[j].isdigit()):
                j += 1
            node = TreeNode(int(s[i:j]))
            if j < len(s) and s[j] == '(':  # left child
                bal = 0
                k = j
                while k < len(s):
                    if s[k] == '(': bal += 1
                    if s[k] == ')': bal -= 1
                    if bal == 0: break
                    k += 1
                node.left = parse(j+1)
                j = k+1
            if j < len(s) and s[j] == '(':  # right child
                bal = 0
                k = j
                while k < len(s):
                    if s[k] == '(': bal += 1
                    if s[k] == ')': bal -= 1
                    if bal == 0: break
                    k += 1
                node.right = parse(j+1)
            return node
        return parse(0)

# Example usage:
sol = Solution()
root = sol.str2tree("4(2(3)(1))(6(5))")
print(root.val)  # Output: 4
