"""
1206. Design Skiplist

Design a Skiplist with add, erase, and search operations. Each operation should have average O(log n) time complexity.

Constraints:
- 0 <= num, target <= 2 * 10^4
- At most 5 * 10^4 calls will be made to the methods.

Example:
Input: ["Skiplist","add","add","add","search","erase","search"], [[],[1],[2],[3],[0],[1],[1]]
Output: [null,null,null,null,false,true,false]

"""
import random
class Node:
    def __init__(self, val, level):
        self.val = val
        self.forward = [None]*level
class Skiplist:
    def __init__(self):
        self.head = Node(-1, 16)
    def search(self, target: int) -> bool:
        node = self.head
        for i in reversed(range(16)):
            while node.forward[i] and node.forward[i].val < target:
                node = node.forward[i]
        node = node.forward[0]
        return node and node.val == target
    def add(self, num: int) -> None:
        update = [None]*16
        node = self.head
        for i in reversed(range(16)):
            while node.forward[i] and node.forward[i].val < num:
                node = node.forward[i]
            update[i] = node
        level = 1
        while level < 16 and random.random() < 0.5:
            level += 1
        new = Node(num, level)
        for i in range(level):
            new.forward[i] = update[i].forward[i]
            update[i].forward[i] = new
    def erase(self, num: int) -> bool:
        update = [None]*16
        node = self.head
        found = False
        for i in reversed(range(16)):
            while node.forward[i] and node.forward[i].val < num:
                node = node.forward[i]
            update[i] = node
        node = node.forward[0]
        if node and node.val == num:
            found = True
            for i in range(16):
                if update[i].forward[i] != node:
                    break
                update[i].forward[i] = node.forward[i]
        return found

# Example usage
if __name__ == "__main__":
    skiplist = Skiplist()
    skiplist.add(1)
    skiplist.add(2)
    skiplist.add(3)
    print(skiplist.search(0))  # Output: False
    print(skiplist.erase(1))   # Output: True
    print(skiplist.search(1))  # Output: False
