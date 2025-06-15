# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

from linked_list_impl import Node 
from linked_list_impl import LinkedList



def addTwoNumbers(l1: LinkedList, l2: LinkedList) -> LinkedList:
    """Adds two numbers represented by linked lists.
    Args:
        l1 (LinkedList): The first linked list representing the first number.
        l2 (LinkedList): The second linked list representing the second number.
    Returns:            
        LinkedList: A new linked list representing the sum of the two numbers.
    """
    l3 = LinkedList()
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.data if l1 else 0
        val2 = l2.data if l2 else 0

        sum_val = val1 + val2 + carry
        carry = sum_val // 10
        digit = sum_val % 10

        l3.insert_at_end(digit)

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return l3.to_list()


ll1 = LinkedList()
ll1.insert_values([2, 4, 3])


ll2 = LinkedList()
ll2.insert_values([5, 6, 4])
result = addTwoNumbers(ll1.head, ll2.head)

print("Result linked list:", result)  # Convert the result linked list to a list for easy printing
print(ll1.sort_linked_list().to_list())
print(ll2.sort_linked_list().to_list())

# Print the result linked list
print("merge sorted:", ll1.merge_sorted(ll2))


