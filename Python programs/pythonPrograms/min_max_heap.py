# Min Heap and Max Heap implementation
import heapq

class MinHeap:
    def __init__(self):
        self.h = []
    def push(self, x):
        heapq.heappush(self.h, x)
    def pop(self):
        return heapq.heappop(self.h)
    def top(self):
        return self.h[0]

class MaxHeap:
    def __init__(self):
        self.h = []
    def push(self, x):
        heapq.heappush(self.h, -x)
    def pop(self):
        return -heapq.heappop(self.h)
    def top(self):
        return -self.h[0]

if __name__ == "__main__":
    minheap = MinHeap(); maxheap = MaxHeap()
    for x in [3,1,4,1,5]:
        minheap.push(x); maxheap.push(x)
    print("MinHeap top:", minheap.top())
    print("MaxHeap top:", maxheap.top())
