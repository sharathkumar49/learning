# Even More Queue Problems (with solutions)
# Filename: Queue_More_Problems.py

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self, val):
        self.buffer.appendleft(val)
    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer) == 0
    def size(self):
        return len(self.buffer)
    def front(self):
        if self.is_empty():
            return None
        return self.buffer[-1]

# 1. Check if a given queue is a palindrome
def is_queue_palindrome(q):
    arr = []
    while not q.is_empty():
        arr.append(q.dequeue())
    return arr == arr[::-1]

# 2. Sort a queue using only queue operations (no extra data structures except recursion)
def sort_queue(q):
    if q.is_empty():
        return
    x = q.dequeue()
    sort_queue(q)
    insert_sorted(q, x)

def insert_sorted(q, x):
    if q.is_empty() or x <= q.front():
        q.enqueue(x)
        return
    y = q.dequeue()
    insert_sorted(q, x)
    q.enqueue(y)

# 3. Find the first negative integer in every window of size k
def first_negative_in_window(arr, k):
    q = deque()
    result = []
    for i in range(len(arr)):
        if arr[i] < 0:
            q.append(i)
        if i >= k - 1:
            while q and q[0] < i - k + 1:
                q.popleft()
            result.append(arr[q[0]] if q else 0)
    return result

# 4. Implement a Deque (Double Ended Queue)
class Deque:
    def __init__(self):
        self.dq = deque()
    def push_front(self, x):
        self.dq.append(x)
    def push_back(self, x):
        self.dq.appendleft(x)
    def pop_front(self):
        if not self.dq:
            print("Deque is empty")
            return None
        return self.dq.pop()
    def pop_back(self):
        if not self.dq:
            print("Deque is empty")
            return None
        return self.dq.popleft()
    def is_empty(self):
        return not self.dq

# 5. Implement a queue that supports getMin() in O(1) time
class MinQueue:
    def __init__(self):
        self.q = deque()
        self.minq = deque()
    def enqueue(self, x):
        self.q.append(x)
        while self.minq and self.minq[-1] > x:
            self.minq.pop()
        self.minq.append(x)
    def dequeue(self):
        if not self.q:
            print("Queue is empty")
            return None
        x = self.q.popleft()
        if x == self.minq[0]:
            self.minq.popleft()
        return x
    def get_min(self):
        if not self.minq:
            print("Queue is empty")
            return None
        return self.minq[0]

if __name__ == '__main__':
    # 1. Palindrome check
    print("Queue Palindrome:")
    q = Queue()
    for x in [1,2,3,2,1]:
        q.enqueue(x)
    print(is_queue_palindrome(q))

    # 2. Sort queue
    print("\nSort Queue:")
    q = Queue()
    for x in [3,1,4,2]:
        q.enqueue(x)
    sort_queue(q)
    while not q.is_empty():
        print(q.dequeue(), end=' ')
    print()

    # 3. First negative in window
    print("\nFirst negative in window:")
    arr = [12, -1, -7, 8, 15, 30, 16, 28]
    print(first_negative_in_window(arr, 3))

    # 4. Deque
    print("\nDeque:")
    dq = Deque()
    dq.push_back(1)
    dq.push_front(2)
    dq.push_back(3)
    print(dq.pop_front())
    print(dq.pop_back())
    print(dq.pop_front())
    print(dq.pop_front())  # Should print empty

    # 5. MinQueue
    print("\nMinQueue:")
    mq = MinQueue()
    mq.enqueue(3)
    mq.enqueue(1)
    mq.enqueue(2)
    print(mq.get_min())
    mq.dequeue()
    print(mq.get_min())
    mq.dequeue()
    print(mq.get_min())
    mq.dequeue()
    print(mq.get_min())  # Should print empty
