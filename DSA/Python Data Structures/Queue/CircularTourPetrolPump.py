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

def circular_tour(petrol, distance):
    n = len(petrol)
    start = 0
    curr_petrol = 0
    prev_petrol = 0
    for i in range(n):
        curr_petrol += petrol[i] - distance[i]
        if curr_petrol < 0:
            start = i + 1
            prev_petrol += curr_petrol
            curr_petrol = 0
    if curr_petrol + prev_petrol >= 0:
        return start
    else:
        return -1

if __name__ == '__main__':
    petrol = [4, 6, 7, 4]
    distance = [6, 5, 3, 5]
    print(circular_tour(petrol, distance))
