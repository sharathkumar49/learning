"""
1188. Design Bounded Blocking Queue

Design a thread-safe bounded blocking queue with enqueue, dequeue, and size operations. Use condition variables for thread synchronization.

Constraints:
- 1 <= capacity <= 1000
- At most 1000 calls to each method.

Example:
Input: ["BoundedBlockingQueue","enqueue","dequeue","size"], [[2],[1],[],[]]
Output: [null,null,1,0]

"""
import threading
from collections import deque
class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        self.q = deque()
        self.capacity = capacity
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)
    def enqueue(self, element: int) -> None:
        with self.not_full:
            while len(self.q) == self.capacity:
                self.not_full.wait()
            self.q.append(element)
            self.not_empty.notify()
    def dequeue(self) -> int:
        with self.not_empty:
            while not self.q:
                self.not_empty.wait()
            val = self.q.popleft()
            self.not_full.notify()
            return val
    def size(self) -> int:
        with self.lock:
            return len(self.q)

# Example usage (single-threaded)
if __name__ == "__main__":
    q = BoundedBlockingQueue(2)
    q.enqueue(1)
    print(q.size())  # Output: 1
    print(q.dequeue())  # Output: 1
    print(q.size())  # Output: 0
