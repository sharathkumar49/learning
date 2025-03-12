import threading
import time

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

binary_queue = Queue()

def add_binary_number(strt, end):
    for i in range(strt, end+1):
        binary_queue.enqueue(bin(i)[2:])


def get_binary_number():
    time.sleep(1)
    while binary_queue.size():
        print(binary_queue.dequeue())
        time.sleep(2)

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=add_binary_number, args=(1,10))
    t2 = threading.Thread(target=get_binary_number)

    t1.start()
    t2.start()
    print(binary_queue.size())