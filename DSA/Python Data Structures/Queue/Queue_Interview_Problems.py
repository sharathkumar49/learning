# Queue Interview Problems (Google, Microsoft, Twitter, etc.)
# Filename: Queue_Interview_Problems.py

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

# 1. Implement a Stack using Queues (Asked in Google, Microsoft)
class StackUsingQueues:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q2.enqueue(x)
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.dequeue()

    def top(self):
        return self.q1.front()

    def empty(self):
        return self.q1.is_empty()

# 2. Generate the first n numbers made up of only 5 and 6 (Twitter)
def generate_numbers_5_6(n):
    q = Queue()
    q.enqueue('5')
    q.enqueue('6')
    result = []
    for _ in range(n):
        curr = q.dequeue()
        result.append(curr)
        q.enqueue(curr + '5')
        q.enqueue(curr + '6')
    return result

# 3. First non-repeating character in a stream (Google, Microsoft)
def first_non_repeating(stream):
    q = Queue()
    freq = {}
    result = []
    for ch in stream:
        freq[ch] = freq.get(ch, 0) + 1
        q.enqueue(ch)
        while not q.is_empty() and freq[q.front()] > 1:
            q.dequeue()
        result.append(q.front() if not q.is_empty() else '#')
    return result

# 4. Reverse the first k elements of a queue (Microsoft)
def reverse_k_elements(q, k):
    stack = []
    for _ in range(k):
        stack.append(q.dequeue())
    while stack:
        q.enqueue(stack.pop())
    for _ in range(q.size() - k):
        q.enqueue(q.dequeue())
    return q

# 5. Interleave the first half of the queue with the second half (Google)
def interleave_queue(q):
    n = q.size()
    stack = []
    for _ in range(n // 2):
        stack.append(q.dequeue())
    while stack:
        q.enqueue(stack.pop())
    for _ in range(n // 2):
        q.enqueue(q.dequeue())
    for _ in range(n // 2):
        stack.append(q.dequeue())
    while stack:
        q.enqueue(stack.pop())
        q.enqueue(q.dequeue())
    return q

if __name__ == '__main__':
    # 1. Stack using Queues
    print("Stack Using Queues:")
    s = StackUsingQueues()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())  # 3
    print(s.top())  # 2

    # 2. Generate numbers with 5 and 6
    print("\nNumbers made up of 5 and 6:")
    print(generate_numbers_5_6(10))

    # 3. First non-repeating character in a stream
    print("\nFirst non-repeating character in stream:")
    stream = "aabc"
    print(first_non_repeating(stream))

    # 4. Reverse first k elements
    print("\nReverse first k elements:")
    q = Queue()
    for i in range(1, 6):
        q.enqueue(i)
    q = reverse_k_elements(q, 3)
    while not q.is_empty():
        print(q.dequeue(), end=' ')
    print()

    # 5. Interleave queue
    print("\nInterleave queue:")
    q = Queue()
    for i in range(1, 7):
        q.enqueue(i)
    q = interleave_queue(q)
    while not q.is_empty():
        print(q.dequeue(), end=' ')
    print()
