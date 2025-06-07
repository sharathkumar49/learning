from linked_list_impl import Node 
from linked_list_impl import LinkedList


ll1 = LinkedList()
ll1.insert_values([2, 4, 3, 9, 24, 34, 1, 0, 2, 3, 4, 5, 6, 7, 8, 9])

ll1.create_cycle(2)  # Create a cycle at node with value '3'

print("Cycle detected?", ll1.has_cycle())  # Should return True


print(ll1.has_cycle())
k = ll1.detect_cycle()  # Should return the node where the cycle starts
print(ll1.find_cycle_start(k).data)  # Should return the node where the cycle starts

ll1.remove_cycle()  # Remove the cycle
print("Cycle detected after removal?", ll1.remove_cycle())  # Should return False