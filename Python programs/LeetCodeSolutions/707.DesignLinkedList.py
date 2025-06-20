"""
LeetCode 707. Design Linked List

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.

Implement the MyLinkedList class:
- MyLinkedList() Initializes the MyLinkedList object.
- int get(int index) Get the value of the index-th node in the linked list. If the index is invalid, return -1.
- void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
- void addAtTail(int val) Append a node of value val as the last element of the linked list.
- void addAtIndex(int index, int val) Add a node of value val before the index-th node in the linked list. If index equals the length of the linked list, the node will be appended to the end. If index is greater than the length, the node will not be inserted.
- void deleteAtIndex(int index) Delete the index-th node in the linked list, if the index is valid.

Example 1:
Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1,2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Constraints:
- 0 <= index, val <= 1000
- Please do not use the built-in LinkedList library.
- At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex, and deleteAtIndex.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.size = 0
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        prev = self.head
        for _ in range(index):
            prev = prev.next
        node = ListNode(val)
        node.next = prev.next
        prev.next = node
        self.size += 1
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        prev = self.head
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        self.size -= 1

# Example usage
if __name__ == "__main__":
    linked = MyLinkedList()
    linked.addAtHead(1)
    linked.addAtTail(3)
    linked.addAtIndex(1, 2)
    print(linked.get(1))  # Output: 2
    linked.deleteAtIndex(1)
    print(linked.get(1))  # Output: 3
