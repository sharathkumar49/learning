# Convert 2D Matrix to Linked List
from linked_list_impl import Node

def matrix_to_linked_list(matrix):
    head = None
    tail = None
    for row in matrix:
        for val in row:
            new_node = Node(val)
            if not head:
                head = tail = new_node
            else:
                tail.next = new_node
                tail = new_node
    return head
# Example usage:
mat = [[1,2,3],[4,5,6],[7,8,9]]
ll_head = matrix_to_linked_list(mat)
# Traverse and print
curr = ll_head
while curr:
    print(curr.data, end=' --> ' if curr.next else '\n')
    curr = curr.next
