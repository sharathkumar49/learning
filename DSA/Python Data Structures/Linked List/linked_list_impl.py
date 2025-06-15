class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:   
						#if you're inserting, you need to modify the 'next' pointer of the previous element 
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
				# you have to stop at the element which is prior to the element that you are trying to remove and in that element, you can modify the links
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
			
			
    def insert_after_value(self, data_after, data_to_insert):
		# Search for first occurance of data_after value in linked list
		# Now insert data_to_insert after data_after node
		
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next


    def remove_by_value(self, data):
		# Remove first node that contains data
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
			
    def reverse(self):
        if self.head is None:
            return

        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def get_middle(self):
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    def create_cycle(self, pos):
        """Creates a cycle by connecting the last node to a previous node at `pos` index."""
        if self.head is None:
            return
        
        last_node = self.head
        cycle_node = None
        index = 0
        current = self.head

        while current:
            if index == pos:
                cycle_node = current
            last_node = current
            current = current.next
            index += 1

        if cycle_node:
            last_node.next = cycle_node  # Create a cycle


    def has_cycle(self):
        print("Checking for cycle in the linked list...")
        print("[2, 4, 3, 9, 24, 34, 1, 0, 2, 3, 4, 5, 6, 7, 8, 9]")
        if self.head is None:
            return False

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            print(slow.data, fast.data)  # Debugging output to trace the values
            if slow == fast:
                return True

        return False    

    def detect_cycle(self):
        """Detects a cycle using Floyd’s Cycle Detection Algorithm."""
        if self.head is None:
            return None

        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow  # Cycle detected; return the meeting point

        return None  # No cycle

    def find_cycle_start(self, meet_point):
        """Finds the starting node of the cycle."""
        ptr1, ptr2 = self.head, meet_point

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1  # Cycle start node
    
    def remove_cycle(self):
        """Removes the cycle from the linked list."""
        meet_point = self.detect_cycle()
        if not meet_point:
            return False  # No cycle to remove

        cycle_start = self.find_cycle_start(meet_point)

        # Traverse until the last node in the cycle
        temp = cycle_start
        while temp.next != cycle_start:
            temp = temp.next
        print(temp.data, temp.next.data, cycle_start.data)  # Debugging output to trace the values
        # print(temp.data, cycle_start.data)  # Debugging output to trace the values
        temp.next = None  # Break the cycle
        return True

    def get_nth_from_end(self, n):
        if self.head is None or n <= 0:
            return None

        first = self.head
        second = self.head

        for _ in range(n):
            if first is None:
                return None
            first = first.next

        while first:
            first = first.next
            second = second.next

        return second.data if second else None

    def merge_sorted(self, other):
        if self.head is None:
            return other.copy()
        if other.head is None:
            return self.copy()

        merged_list = LinkedList()
        self = self.sort_linked_list()
        other = other.sort_linked_list()
        itr1 = self.head
        itr2 = other.head

        while itr1 and itr2:
            if itr1.data < itr2.data:
                print("condition 1, itr1.data < itr2.data")
                print("itr1.data:", itr1.data)
                merged_list.insert_at_end(itr1.data)
                itr1 = itr1.next
            else:
                print("condition 2, itr1.data >= itr2.data")
                print("itr2.data:", itr2.data)
                merged_list.insert_at_end(itr2.data)
                itr2 = itr2.next
        # If one list is exhausted, append the remaining elements of the other list
        while itr1:
            merged_list.insert_at_end(itr1.data)
            itr1 = itr1.next
        # If the second list is exhausted, append the remaining elements of the first list
        while itr2:
            merged_list.insert_at_end(itr2.data)
            itr2 = itr2.next

        return merged_list
    
    def merge_two_sorted_lists(self, other):
         if sorted(self.to_list) and sorted(other.to_list):
            return self.merge_sorted(other)
         else:
            raise ValueError("Both linked lists must be sorted before merging")
                 
    
    def to_list(self):
        result = []
        itr = self.head
        while itr:
            result.append(itr.data)
            itr = itr.next
        return result
    
    def from_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def __iter__(self):
        itr = self.head
        while itr:
            yield itr.data
            itr = itr.next

    def __str__(self):
        return ' --> '.join(str(data) for data in self) if self.head else 'Linked list is empty'
    
    def __len__(self):
        return self.get_length()
    
    def __getitem__(self, index):
        if index < 0 or index >= self.get_length():
            raise IndexError("Index out of bounds")
        
        itr = self.head
        for _ in range(index):
            itr = itr.next
        return itr.data if itr else None
    
    def __setitem__(self, index, value):
        if index < 0 or index >= self.get_length():
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.head.data = value
            return
        
        itr = self.head
        for _ in range(index - 1):
            itr = itr.next
        if itr and itr.next:
            itr.next.data = value
        else:
            raise IndexError("Index out of bounds")

    def __contains__(self, value):
        itr = self.head
        while itr:
            if itr.data == value:
                return True
            itr = itr.next
        return False
    
    def __eq__(self, other):
        if not isinstance(other, LinkedList):
            return False
        
        self_itr = self.head
        other_itr = other.head
        
        while self_itr and other_itr:
            if self_itr.data != other_itr.data:
                return False
            self_itr = self_itr.next
            other_itr = other_itr.next
        
        return self_itr is None and other_itr is None
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __add__(self, other):
        if not isinstance(other, LinkedList):
            raise TypeError("Can only add another LinkedList")
        
        new_list = LinkedList()
        new_list.head = self.head
        
        if not new_list.head:
            new_list.head = other.head
            return new_list
        
        itr = new_list.head
        while itr.next:
            itr = itr.next
        
        itr.next = other.head
        return new_list
    
    def __iadd__(self, other):
        if not isinstance(other, LinkedList):
            raise TypeError("Can only add another LinkedList")
        
        if not self.head:
            self.head = other.head
            return self
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = other.head
        return self
    
    def __repr__(self):
        return f"LinkedList({self.to_list()})"
    
    def __bool__(self):
        return self.head is not None
    
    def clear(self):
        self.head = None
        return self
    
    def copy(self):
        new_list = LinkedList()
        if not self.head:
            return new_list
        
        new_list.head = Node(self.head.data)
        current_new = new_list.head
        current_old = self.head.next
        
        while current_old:
            current_new.next = Node(current_old.data)
            current_new = current_new.next
            current_old = current_old.next
        
        return new_list
    
    def sort_linked_list(self):
        sorted_list = sorted(self.to_list())
        new_linked_list = LinkedList()
        for val in sorted_list:
            new_linked_list.insert_at_end(val)
        return new_linked_list


    def get_middle_node(self, head):
        if head is None:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
        
    def find(self, value):
        if self.head is None:
            return None

        itr = self.head
        while itr:
            if itr.data == value:
                return itr
            itr = itr.next

        return None
    

    def find_index(self, value):
        if self.head is None:
            return -1

        index = 0
        itr = self.head
        while itr:
            if itr.data == value:
                return index
            itr = itr.next
            index += 1

        return -1
    
    def remove_duplicates(self):
        if self.head is None:
            return

        seen = set()
        current = self.head
        seen.add(current.data)

        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next

    def split(self):
        if self.head is None or self.head.next is None:
            return LinkedList(), LinkedList()

        slow = self.head
        fast = self.head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None

        first_half = LinkedList()
        second_half = LinkedList()
        first_half.head = self.head
        second_half.head = slow

        return first_half, second_half
    
    def rotate(self, k):
        if self.head is None or k <= 0:
            return

        length = self.get_length()
        k = k % length

        if k == 0:
            return

        slow = self.head
        fast = self.head

        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        slow.next = None
        fast.next = self.head
        self.head = new_head

    def is_palindrome(self):
        if self.head is None or self.head.next is None:
            return True

        slow = self.head
        fast = self.head
        stack = []

        while fast and fast.next:
            stack.append(slow.data)
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next
        while slow:
            if stack.pop() != slow.data:
                return False
            slow = slow.next
        return True
    
    def kth_to_last(self, k):
        if self.head is None or k <= 0:
            return None

        first = self.head
        second = self.head

        for _ in range(k):
            if first is None:
                return None
            first = first.next

        while first:
            first = first.next
            second = second.next

        return second.data if second else None
    
    def remove_duplicates_sorted(self):
        if self.head is None:
            return

        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

    def find_intersection(self, other):
        if self.head is None or other.head is None:
            return None

        len1 = self.get_length()
        len2 = other.get_length()

        diff = abs(len1 - len2)
        longer = self.head if len1 > len2 else other.head
        shorter = other.head if len1 > len2 else self.head

        for _ in range(diff):
            longer = longer.next

        while longer and shorter:
            if longer == shorter:
                return longer.data
            longer = longer.next
            shorter = shorter.next

        return None
    