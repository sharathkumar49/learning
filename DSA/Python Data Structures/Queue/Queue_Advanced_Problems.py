# More Advanced Queue Problems (with solutions)
# Filename: Queue_Advanced_Problems.py

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

# 1. Implement a Circular Queue (Fixed size)
class CircularQueue:
    def __init__(self, k):
        self.q = [None]*k
        self.maxlen = k
        self.front = 0
        self.rear = 0
        self.count = 0
    def enqueue(self, val):
        if self.count == self.maxlen:
            print("Circular Queue is full")
            return False
        self.q[self.rear] = val
        self.rear = (self.rear + 1) % self.maxlen
        self.count += 1
        return True
    def dequeue(self):
        if self.count == 0:
            print("Circular Queue is empty")
            return None
        val = self.q[self.front]
        self.front = (self.front + 1) % self.maxlen
        self.count -= 1
        return val
    def is_empty(self):
        return self.count == 0
    def is_full(self):
        return self.count == self.maxlen

# 2. Implement a Queue using Two Stacks
class QueueUsingStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def enqueue(self, x):
        self.s1.append(x)
    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            print("Queue is empty")
            return None
        return self.s2.pop()
    def is_empty(self):
        return not self.s1 and not self.s2

# 3. Find the maximum in every window of size k in an array (Sliding Window Maximum)
def max_sliding_window(arr, k):
    q = deque()
    result = []
    for i, num in enumerate(arr):
        while q and q[0] <= i - k:
            q.popleft()
        while q and arr[q[-1]] < num:
            q.pop()
        q.append(i)
        if i >= k - 1:
            result.append(arr[q[0]])
    return result

# 4. Rotten Oranges (Minimum time to rot all oranges in a grid)
def oranges_rotting(grid):
    from collections import deque
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1
    time = 0
    while q:
        r, c, t = q.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                grid[nr][nc]=2
                fresh -= 1
                q.append((nr, nc, t+1))
                time = t+1
    return time if fresh==0 else -1

# 5. Implement a Priority Queue using heapq
import heapq
class PriorityQueue:
    def __init__(self):
        self.heap = []
    def enqueue(self, val, priority):
        heapq.heappush(self.heap, (priority, val))
    def dequeue(self):
        if not self.heap:
            print("Priority Queue is empty")
            return None
        return heapq.heappop(self.heap)[1]
    def is_empty(self):
        return not self.heap

if __name__ == '__main__':
    # 1. Circular Queue
    print("Circular Queue:")
    cq = CircularQueue(3)
    print(cq.enqueue(1))
    print(cq.enqueue(2))
    print(cq.enqueue(3))
    print(cq.enqueue(4))  # Should print full
    print(cq.dequeue())
    print(cq.enqueue(4))
    print(cq.dequeue())
    print(cq.dequeue())
    print(cq.dequeue())
    print(cq.dequeue())  # Should print empty

    # 2. Queue using Stacks
    print("\nQueue using Stacks:")
    qs = QueueUsingStacks()
    qs.enqueue(10)
    qs.enqueue(20)
    print(qs.dequeue())
    qs.enqueue(30)
    print(qs.dequeue())
    print(qs.dequeue())
    print(qs.dequeue())  # Should print empty

    # 3. Sliding Window Maximum
    print("\nSliding Window Maximum:")
    arr = [1,3,-1,-3,5,3,6,7]
    print(max_sliding_window(arr, 3))

    # 4. Rotten Oranges
    print("\nRotten Oranges:")
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(oranges_rotting(grid))

    # 5. Priority Queue
    print("\nPriority Queue:")
    pq = PriorityQueue()
    pq.enqueue('task1', 2)
    pq.enqueue('task2', 1)
    pq.enqueue('task3', 3)
    while not pq.is_empty():
        print(pq.dequeue())
