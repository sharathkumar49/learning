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

class UndoRedo:
    def __init__(self):
        self.undo_stack = Stack()
        self.redo_stack = Stack()
    def do(self, action):
        self.undo_stack.push(action)
        self.redo_stack = Stack()  # Clear redo stack
    def undo(self):
        if not self.undo_stack.is_empty():
            action = self.undo_stack.pop()
            self.redo_stack.push(action)
            return action
        return None
    def redo(self):
        if not self.redo_stack.is_empty():
            action = self.redo_stack.pop()
            self.undo_stack.push(action)
            return action
        return None

# Example usage
if __name__ == "__main__":
    ur = UndoRedo()
    ur.do("type A")
    ur.do("type B")
    print(ur.undo())  # type B
    print(ur.undo())  # type A
    print(ur.redo())  # type A
    print(ur.redo())  # type B
