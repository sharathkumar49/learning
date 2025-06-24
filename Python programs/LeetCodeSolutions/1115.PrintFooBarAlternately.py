"""
1115. Print FooBar Alternately

Suppose two threads are running concurrently. One thread prints "foo" and the other prints "bar". Print "foobar" n times, alternating between the two threads.

Constraints:
- 1 <= n <= 1000

Example:
Input: n = 2
Output: "foobarfoobar"
"""
import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_event = threading.Event()
        self.bar_event = threading.Event()
        self.foo_event.set()

    def foo(self, printFoo):
        for _ in range(self.n):
            self.foo_event.wait()
            printFoo()
            self.foo_event.clear()
            self.bar_event.set()

    def bar(self, printBar):
        for _ in range(self.n):
            self.bar_event.wait()
            printBar()
            self.bar_event.clear()
            self.foo_event.set()

# Example usage:
# foobar = FooBar(2)
# from threading import Thread
# Thread(target=foobar.foo, args=(lambda: print("foo", end=''),)).start()
# Thread(target=foobar.bar, args=(lambda: print("bar", end=''),)).start()
