"""
1116. Print Zero Even Odd

Suppose you are given a class ZeroEvenOdd with a method zero(), even(), and odd(). The same instance will be passed to three different threads. Implement the methods to print a sequence of numbers: 0,1,0,2,0,3,... up to n.

Constraints:
- 1 <= n <= 1000

Example:
Input: n = 2
Output: "0102"
"""
import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_event = threading.Event()
        self.even_event = threading.Event()
        self.odd_event = threading.Event()
        self.zero_event.set()
        self.count = 1

    def zero(self, printNumber):
        for _ in range(self.n):
            self.zero_event.wait()
            printNumber(0)
            self.zero_event.clear()
            if self.count % 2 == 0:
                self.even_event.set()
            else:
                self.odd_event.set()

    def even(self, printNumber):
        for _ in range(2, self.n+1, 2):
            self.even_event.wait()
            printNumber(self.count)
            self.count += 1
            self.even_event.clear()
            self.zero_event.set()

    def odd(self, printNumber):
        for _ in range(1, self.n+1, 2):
            self.odd_event.wait()
            printNumber(self.count)
            self.count += 1
            self.odd_event.clear()
            self.zero_event.set()

# Example usage:
# zeroEvenOdd = ZeroEvenOdd(2)
# from threading import Thread
# Thread(target=zeroEvenOdd.zero, args=(lambda x: print(x, end=''),)).start()
# Thread(target=zeroEvenOdd.even, args=(lambda x: print(x, end=''),)).start()
# Thread(target=zeroEvenOdd.odd, args=(lambda x: print(x, end=''),)).start()
