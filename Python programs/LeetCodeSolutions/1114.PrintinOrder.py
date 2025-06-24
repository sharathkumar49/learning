"""
1114. Print in Order

Suppose we have a class Foo with three methods: first(), second(), and third(). The same instance of Foo will be passed to three different threads. Implement the methods to ensure that second() is executed after first(), and third() is executed after second().

Constraints:
- The input is a sequence of calls to first(), second(), and third() from three different threads.
- There are no return values for these methods.

Example:
Input: ["Foo","first","second","third"]
Output: [null,"first","second","third"]
"""
import threading

class Foo:
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst):
        printFirst()
        self.first_done.set()

    def second(self, printSecond):
        self.first_done.wait()
        printSecond()
        self.second_done.set()

    def third(self, printThird):
        self.second_done.wait()
        printThird()

# Example usage:
# foo = Foo()
# from threading import Thread
# Thread(target=foo.first, args=(lambda: print("first"),)).start()
# Thread(target=foo.second, args=(lambda: print("second"),)).start()
# Thread(target=foo.third, args=(lambda: print("third"),)).start()
