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

def sum_of_min_max_all_subarrays_k(arr, k):
    n = len(arr)
    maxDeque = deque()
    minDeque = deque()
    total = 0
    for i in range(k):
        while maxDeque and arr[i] >= arr[maxDeque[-1]]:
            maxDeque.pop()
        while minDeque and arr[i] <= arr[minDeque[-1]]:
            minDeque.pop()
        maxDeque.append(i)
        minDeque.append(i)
    for i in range(k, n):
        total += arr[maxDeque[0]] + arr[minDeque[0]]
        while maxDeque and maxDeque[0] <= i - k:
            maxDeque.popleft()
        while minDeque and minDeque[0] <= i - k:
            minDeque.popleft()
        while maxDeque and arr[i] >= arr[maxDeque[-1]]:
            maxDeque.pop()
        while minDeque and arr[i] <= arr[minDeque[-1]]:
            minDeque.pop()
        maxDeque.append(i)
        minDeque.append(i)
    total += arr[maxDeque[0]] + arr[minDeque[0]]
    return total

if __name__ == '__main__':
    arr = [2, 5, -1, 7, -3, -1, -2]
    print(sum_of_min_max_all_subarrays_k(arr, 4))
