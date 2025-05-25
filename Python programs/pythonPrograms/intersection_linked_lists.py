# Intersection node of two linked lists
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_intersection_node(headA, headB):
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a

if __name__ == "__main__":
    # Example usage
    a1 = ListNode(1); a2 = ListNode(2); c1 = ListNode(3)
    b1 = ListNode(4); b2 = ListNode(5)
    a1.next = a2; a2.next = c1
    b1.next = b2; b2.next = c1
    print(get_intersection_node(a1, b1).val)
