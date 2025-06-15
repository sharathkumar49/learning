from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self, val):
        self.buffer.appendleft(val)
    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)

def sliding_window_maximum(arr, k):
    Qi = deque()
    result = []
    for i in range(k):
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    for i in range(k, len(arr)):
        result.append(arr[Qi[0]])
        while Qi and Qi[0] <= i - k:
            Qi.popleft()
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    result.append(arr[Qi[0]])
    return result

if __name__ == '__main__':
    arr = [1,3,-1,-3,5,3,6,7]
    print(sliding_window_maximum(arr, 3))
