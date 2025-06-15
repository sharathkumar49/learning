# Split Linked List into k Parts
# Split the linked list into k consecutive parts as evenly as possible.
from linked_list_impl import Node, LinkedList

def split_list_to_parts(head, k):
    # Count length
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    part_size, extra = divmod(length, k)
    parts = []
    curr = head
    for i in range(k):
        head_part = curr
        size = part_size + (1 if i < extra else 0)
        for j in range(size - 1):
            if curr:
                curr = curr.next
        if curr:
            next_part = curr.next
            curr.next = None
            curr = next_part
        parts.append(head_part)
    return parts

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,4,5,6,7,8,9,10])
parts = split_list_to_parts(ll.head, 3)
for idx, part in enumerate(parts):
    l = LinkedList()
    l.head = part
    print(f"Part {idx+1}:", l.to_list())
# Output: [1,2,3,4], [5,6,7], [8,9,10]
