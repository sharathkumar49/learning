# Multiply Two Numbers Represented by Linked Lists
from linked_list_impl import Node, LinkedList

def linked_list_to_number(head):
    num = 0
    multiplier = 1
    while head:
        num += head.data * multiplier
        multiplier *= 10
        head = head.next
    return num

def number_to_linked_list(num):
    if num == 0:
        return Node(0)
    head = None
    while num > 0:
        digit = num % 10
        new_node = Node(digit)
        new_node.next = head
        head = new_node
        num //= 10
    # Reverse to match the input format (least significant digit first)
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def multiply_two_numbers(l1, l2):
    n1 = linked_list_to_number(l1)
    n2 = linked_list_to_number(l2)
    product = n1 * n2
    return number_to_linked_list(product)

# Example usage:
ll1 = LinkedList(); ll1.insert_values([3,4,2])  # 243
ll2 = LinkedList(); ll2.insert_values([4,6,5])  # 564
result_head = multiply_two_numbers(ll1.head, ll2.head)
result = LinkedList(); result.head = result_head
result.print()  # Output: 2 --> 5 --> 0 --> 7 --> 3 --> 1 (243*564=137052)
