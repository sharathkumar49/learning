"""
LeetCode 708. Insert into a Sorted Circular Linked List

Given a Circular Linked List node, which is sorted in non-descending order, write a function to insert a value into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not be the smallest value in the list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the linked list should remain circular.

If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the original given node.

Example 1:
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]

Example 2:
Input: head = [], insertVal = 1
Output: [1]

Constraints:
- 0 <= Number of nodes <= 5 * 10^4
- -10^6 <= Node.val <= 10^6
- All values of the linked list are unique.
- At most one node will be given as a reference to the list.
"""
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def insert(head: 'Node', insertVal: int) -> 'Node':
    new_node = Node(insertVal)
    if not head:
        new_node.next = new_node
        return new_node
    prev, curr = head, head.next
    while True:
        if prev.val <= insertVal <= curr.val:
            break
        if prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val):
            break
        prev, curr = curr, curr.next
        if prev == head:
            break
    prev.next = new_node
    new_node.next = curr
    return head

# Example usage
if __name__ == "__main__":
    # Helper to print circular list
    def print_circular(head):
        vals = []
        curr = head
        while True:
            vals.append(curr.val)
            curr = curr.next
            if curr == head:
                break
        print(vals)
    n1 = Node(3)
    n2 = Node(4)
    n3 = Node(1)
    n1.next = n2
    n2.next = n3
    n3.next = n1
    head = insert(n1, 2)
    print_circular(head)  # Output: [3, 4, 1, 2] (order may vary)
    head2 = insert(None, 1)
    print_circular(head2)  # Output: [1]
