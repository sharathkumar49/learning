# Find the Maximum Sum Path Across Two Sorted Linked Lists
from linked_list_impl import Node, LinkedList

def max_sum_path(head1, head2):
    result = None
    last = None
    sum1 = sum2 = 0
    curr1, curr2 = head1, head2
    start1, start2 = head1, head2
    while curr1 or curr2:
        if curr1 and (not curr2 or curr1.data < curr2.data):
            sum1 += curr1.data
            curr1 = curr1.next
        elif curr2 and (not curr1 or curr2.data < curr1.data):
            sum2 += curr2.data
            curr2 = curr2.next
        else:
            # Common node
            sum1 += curr1.data
            sum2 += curr2.data
            if sum1 > sum2:
                if not result:
                    result = start1
                else:
                    last.next = start1
                last = curr1
            else:
                if not result:
                    result = start2
                else:
                    last.next = start2
                last = curr2
            start1 = curr1.next
            start2 = curr2.next
            sum1 = sum2 = 0
            curr1 = curr1.next
            curr2 = curr2.next
    # Attach remaining
    if sum1 > sum2:
        if not result:
            result = start1
        else:
            last.next = start1
    else:
        if not result:
            result = start2
        else:
            last.next = start2
    return result

# Example usage:
ll1 = LinkedList(); ll1.insert_values([1,3,30,90,120,240,511])
ll2 = LinkedList(); ll2.insert_values([0,3,12,32,90,125,240,249])
res_head = max_sum_path(ll1.head, ll2.head)
res = LinkedList(); res.head = res_head
res.print()  # Output: path with max sum
