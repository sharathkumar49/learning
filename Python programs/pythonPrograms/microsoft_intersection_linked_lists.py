# Microsoft: Find the Intersection Node of Two Linked Lists
# Write a program to find the node at which the intersection of two singly linked lists begins.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a

if __name__ == "__main__":
    # Example usage
    a = ListNode(4)
    b = ListNode(1)
    c = ListNode(8)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    x = ListNode(5)
    y = ListNode(6)
    z = ListNode(1)
    x.next = y
    y.next = z
    z.next = c
    print(get_intersection_node(a, x).val)  # Output: 8
