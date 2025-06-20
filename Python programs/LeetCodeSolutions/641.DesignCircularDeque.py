"""
641. Design Circular Deque
Difficulty: Medium

Design your implementation of the circular double-ended queue (deque). Implement the MyCircularDeque class:
- MyCircularDeque(k): Initializes the deque with a maximum size of k.
- insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
- insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
- deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
- deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
- getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
- getRear(): Gets the last item from Deque. If the deque is empty, return -1.
- isEmpty(): Checks whether Deque is empty or not.
- isFull(): Checks whether Deque is full or not.

Example:
Input: ["MyCircularDeque","insertLast","insertLast","insertFront","insertFront","getRear","isFull","deleteLast","insertFront","getFront"]
[[3],[1],[2],[3],[4],[],[],[],[4],[]]
Output: [null,true,true,true,false,2,true,true,true,4]

Constraints:
1 <= k <= 1000
At most 2000 calls will be made to the methods.
"""

class MyCircularDeque:
    def __init__(self, k: int):
        self.q = [0] * k
        self.k = k
        self.head = 0
        self.tail = 0
        self.count = 0
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head = (self.head - 1 + self.k) % self.k
        self.q[self.head] = value
        self.count += 1
        return True
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        self.count += 1
        return True
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.k
        self.count -= 1
        return True
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail - 1 + self.k) % self.k
        self.count -= 1
        return True
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head]
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.tail - 1 + self.k) % self.k]
    def isEmpty(self) -> bool:
        return self.count == 0
    def isFull(self) -> bool:
        return self.count == self.k

# Example usage
# dq = MyCircularDeque(3)
# print(dq.insertLast(1))  # True
# print(dq.insertLast(2))  # True
# print(dq.insertFront(3)) # True
# print(dq.insertFront(4)) # False
# print(dq.getRear())      # 2
# print(dq.isFull())       # True
# print(dq.deleteLast())   # True
# print(dq.insertFront(4)) # True
# print(dq.getFront())     # 4
