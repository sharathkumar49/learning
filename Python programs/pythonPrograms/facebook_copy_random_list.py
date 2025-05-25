# Facebook: Copy List with Random Pointer
# A linked list is given such that each node contains an additional random pointer. Return a deep copy of the list.
class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list(head):
    if not head:
        return None
    old_to_new = {}
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next
    curr = head
    while curr:
        old_to_new[curr].next = old_to_new.get(curr.next)
        old_to_new[curr].random = old_to_new.get(curr.random)
        curr = curr.next
    return old_to_new[head]

if __name__ == "__main__":
    # Example usage
    a = Node(1)
    b = Node(2)
    a.next = b
    a.random = b
    b.random = b
    res = copy_random_list(a)
    print(res.val, res.random.val)  # Output: 1 2
    print(res.next.val, res.next.random.val)  # Output: 2 2
