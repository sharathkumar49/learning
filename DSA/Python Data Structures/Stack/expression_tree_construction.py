from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)

class ExprTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def construct_expression_tree(postfix):
    stack = Stack()
    for token in postfix:
        if token not in '+-*/':
            stack.push(ExprTreeNode(token))
        else:
            right = stack.pop()
            left = stack.pop()
            node = ExprTreeNode(token)
            node.left = left
            node.right = right
            stack.push(node)
    return stack.pop()

def inorder(node):
    if not node:
        return ''
    if not node.left and not node.right:
        return str(node.val)
    return '(' + inorder(node.left) + str(node.val) + inorder(node.right) + ')'

# Example usage
if __name__ == "__main__":
    postfix = ['3', '4', '+', '2', '*', '7', '/']
    root = construct_expression_tree(postfix)
    print(inorder(root))  # ((3+4)*2)/7
