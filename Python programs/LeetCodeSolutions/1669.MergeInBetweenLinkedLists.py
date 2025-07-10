"""
LeetCode 1669. Merge In Between Linked Lists

Given two linked lists list1 and list2, and two integers a and b, merge list2 into list1 between positions a and b.

Example 1:
Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [0,1,2,1000000,1000001,1000002,5]

Constraints:
- 3 <= list1.length <= 10^4
- 1 <= a <= b < list1.length - 1
- 1 <= list2.length <= 10^4
"""

def mergeInBetween(list1, a, b, list2):
    head = list1
    for _ in range(a-1):
        list1 = list1.next
    tail = list1
    for _ in range(b-a+2):
        tail = tail.next
    list1.next = list2
    while list2.next:
        list2 = list2.next
    list2.next = tail
    return head

# Example usage:
# (Assume ListNode class is defined)
# list1 = ...
# list2 = ...
# a = ...
# b = ...
# print(mergeInBetween(list1, a, b, list2))
