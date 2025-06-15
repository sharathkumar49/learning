# Program: Implement k Queues in a Single Array
# Problem: Design a data structure to implement k queues in a single array of size n.

class KQueues:
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.arr = [0]*n
        self.front = [-1]*k
        self.rear = [-1]*k
        self.next = list(range(1, n)) + [-1]
        self.free = 0
    def enqueue(self, item, qn):
        if self.free == -1:
            print('Queue Overflow')
            return
        i = self.free
        self.free = self.next[i]
        if self.front[qn] == -1:
            self.front[qn] = i
        else:
            self.next[self.rear[qn]] = i
        self.next[i] = -1
        self.rear[qn] = i
        self.arr[i] = item
    def dequeue(self, qn):
        if self.front[qn] == -1:
            print('Queue Underflow')
            return None
        i = self.front[qn]
        self.front[qn] = self.next[i]
        self.next[i] = self.free
        self.free = i
        return self.arr[i]

if __name__ == '__main__':
    kq = KQueues(3, 10)
    kq.enqueue(15, 2)
    kq.enqueue(45, 2)
    kq.enqueue(17, 1)
    kq.enqueue(49, 1)
    kq.enqueue(39, 0)
    print(kq.dequeue(2))
    print(kq.dequeue(1))
    print(kq.dequeue(0))
