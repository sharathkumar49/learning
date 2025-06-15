# Check if a Linked List is a Palindrome Using Recursion
from linked_list_impl import Node, LinkedList

def is_palindrome_recursive(head):
    def helper(right):
        nonlocal left
        if not right:
            return True
        res = helper(right.next) and (left.data == right.data)
        left = left.next
        return res
    left = head
    return helper(head)

# Example usage:
ll = LinkedList(); ll.insert_values([1,2,3,2,1])
print('Is palindrome (recursive):', is_palindrome_recursive(ll.head))  # Output: True
