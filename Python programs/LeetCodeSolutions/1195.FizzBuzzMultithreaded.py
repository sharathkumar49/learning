"""
1195. Fizz Buzz Multithreaded

You have four threads: one prints "fizz", another "buzz", another "fizzbuzz", and another prints the numbers. Implement a class FizzBuzz that synchronizes the threads to print the correct output for numbers from 1 to n.

Constraints:
- 1 <= n <= 50

Example:
Input: n = 15
Output: "1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz"

"""
import threading
class FizzBuzz:
    def __init__(self, n):
        self.n = n
        self.i = 1
        self.lock = threading.Lock()
    def fizz(self, printFizz):
        while True:
            with self.lock:
                if self.i > self.n:
                    return
                if self.i % 3 == 0 and self.i % 5 != 0:
                    printFizz()
                    self.i += 1
    def buzz(self, printBuzz):
        while True:
            with self.lock:
                if self.i > self.n:
                    return
                if self.i % 5 == 0 and self.i % 3 != 0:
                    printBuzz()
                    self.i += 1
    def fizzbuzz(self, printFizzBuzz):
        while True:
            with self.lock:
                if self.i > self.n:
                    return
                if self.i % 15 == 0:
                    printFizzBuzz()
                    self.i += 1
    def number(self, printNumber):
        while True:
            with self.lock:
                if self.i > self.n:
                    return
                if self.i % 3 != 0 and self.i % 5 != 0:
                    printNumber(self.i)
                    self.i += 1

# Example usage (single-threaded simulation):
if __name__ == "__main__":
    fb = FizzBuzz(15)
    def printFizz(): print("fizz", end=' ')
    def printBuzz(): print("buzz", end=' ')
    def printFizzBuzz(): print("fizzbuzz", end=' ')
    def printNumber(x): print(x, end=' ')
    # In real use, these would be run in separate threads
    for _ in range(15):
        fb.fizz(printFizz)
        fb.buzz(printBuzz)
        fb.fizzbuzz(printFizzBuzz)
        fb.number(printNumber)
    print()
