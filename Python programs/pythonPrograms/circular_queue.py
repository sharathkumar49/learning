# Circular queue implementation
class CircularQueue:
    def __init__(self, k):
        self.q = [None]*k
        self.head = self.tail = -1
        self.size = k
    def enQueue(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.q[self.tail] = value
        return True
    def deQueue(self):
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        return True
    def Front(self):
        return -1 if self.isEmpty() else self.q[self.head]
    def Rear(self):
        return -1 if self.isEmpty() else self.q[self.tail]
    def isEmpty(self):
        return self.head == -1
    def isFull(self):
        return (self.tail + 1) % self.size == self.head

if __name__ == "__main__":
    cq = CircularQueue(3)
    print(cq.enQueue(1))
    print(cq.enQueue(2))
    print(cq.enQueue(3))
    print(cq.enQueue(4))
    print(cq.Rear())
    print(cq.isFull())
    print(cq.deQueue())
    print(cq.enQueue(4))
    print(cq.Rear())
