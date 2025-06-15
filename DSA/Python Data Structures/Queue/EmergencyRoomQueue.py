from collections import deque
import heapq

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

class EmergencyRoomQueue:
    def __init__(self):
        self.heap = []
        self.count = 0
    def arrive(self, patient, severity):
        heapq.heappush(self.heap, (-severity, self.count, patient))
        self.count += 1
    def treat(self):
        if not self.heap:
            print('No patients in queue')
            return None
        return heapq.heappop(self.heap)[2]
    def is_empty(self):
        return not self.heap

if __name__ == '__main__':
    erq = EmergencyRoomQueue()
    erq.arrive('Patient1', 2)
    erq.arrive('Patient2', 5)
    erq.arrive('Patient3', 3)
    while not erq.is_empty():
        print(erq.treat())
