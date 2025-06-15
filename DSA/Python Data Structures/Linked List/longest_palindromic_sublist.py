# Find the Length of the Longest Palindromic Sublist
from linked_list_impl import Node, LinkedList

def count_common(left, right):
    count = 0
    while left and right:
        if left.data == right.data:
            count += 1
            left = left.next
            right = right.next
        else:
            break
    return count

def longest_palindromic_sublist(head):
    result = 0
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        # Odd length palindrome
        result = max(result, 2 * count_common(prev, next) + 1)
        # Even length palindrome
        result = max(result, 2 * count_common(curr, next))
        prev = curr
        curr = next
    return result

# Example usage:
ll = LinkedList(); ll.insert_values([2,3,7,3,2,12,24])
print('Longest palindromic sublist length:', longest_palindromic_sublist(ll.head))  # Output: 5
