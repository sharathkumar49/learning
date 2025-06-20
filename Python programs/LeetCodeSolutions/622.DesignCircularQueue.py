"""
622. Design Circular Queue
Difficulty: Medium

Design your implementation of the circular queue. Implement the MyCircularQueue class:
- MyCircularQueue(k) Initializes the object with the size of the queue to be k.
- Front() Gets the front item from the queue. If the queue is empty, return -1.
- Rear() Gets the last item from the queue. If the queue is empty, return -1.
- enQueue(value) Inserts an element into the circular queue. Return true if the operation is successful.
- deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
- isEmpty() Checks whether the circular queue is empty or not.
- isFull() Checks whether the circular queue is full or not.

Example:
Input: ["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]
[[3],[1],[2],[3],[4],[],[],[],[4],[]]
Output: [null,true,true,true,false,3,true,true,true,4]

Constraints:
1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to the methods of MyCircularQueue.
"""

class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [0] * k
        self.k = k
        self.head = 0
        self.count = 0
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        tail = (self.head + self.count) % self.k
        self.q[tail] = value
        self.count += 1
        return True
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.k
        self.count -= 1
        return True
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head]
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.head + self.count - 1) % self.k]
    def isEmpty(self) -> bool:
        return self.count == 0
    def isFull(self) -> bool:
        return self.count == self.k

# Example usage
# q = MyCircularQueue(3)
# print(q.enQueue(1))  # True
# print(q.enQueue(2))  # True
# print(q.enQueue(3))  # True
# print(q.enQueue(4))  # False
# print(q.Rear())      # 3
# print(q.isFull())    # True
# print(q.deQueue())   # True
# print(q.enQueue(4))  # True
# print(q.Rear())      # 4
