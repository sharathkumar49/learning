# Facebook: Add two numbers as linked lists (reverse order)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        total = v1 + v2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next

if __name__ == "__main__":
    # Example: 243 + 564 = 807
    a = ListNode(2, ListNode(4, ListNode(3)))
    b = ListNode(5, ListNode(6, ListNode(4)))
    res = add_two_numbers(a, b)
    while res:
        print(res.val, end=' ')
        res = res.next
