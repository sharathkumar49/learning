"""
LeetCode 1265. Print Immutable Linked List in Reverse

You are given an immutable singly linked list, print out the values of each node in reverse with O(1) extra space.

The ImmutableListNode interface is defined as follows:
class ImmutableListNode:
    def printValue(self): # print the value of this node.
    def getNext(self): # return the next node.

Constraints:
- The linked list has between 1 and 1000 nodes.
- The value of each node is between 0 and 1000.

Note: You cannot modify the list or use extra space proportional to the list size.

"""
# The ImmutableListNode API is not implemented here. This is a template for LeetCode submission.
def printLinkedListInReverse(head):
    def getLength(node):
        length = 0
        while node:
            length += 1
            node = node.getNext()
        return length
    def printReverse(node, length):
        if length == 0:
            return
        printReverse(node.getNext(), length - 1)
        node.printValue()
    length = getLength(head)
    printReverse(head, length)

# Example usage:
# Not executable here as ImmutableListNode is not implemented.
