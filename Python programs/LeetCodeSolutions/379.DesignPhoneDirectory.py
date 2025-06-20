"""
379. Design Phone Directory

Design a phone directory that manages the allocation and release of phone numbers.

Implement the PhoneDirectory class:
- PhoneDirectory(int maxNumbers) Initializes the phone directory with the numbers 0 to maxNumbers - 1.
- int get() Provides a number that is not assigned to anyone. Returns -1 if none is available.
- bool check(int number) Returns true if the number is available or false if it is already assigned.
- void release(int number) Recycles or releases a number.

Constraints:
- 1 <= maxNumbers <= 10^4
- At most 2 * 10^4 calls will be made to get, check, and release.
"""
from collections import deque

class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        self.available = set(range(maxNumbers))
        self.queue = deque(range(maxNumbers))
    def get(self) -> int:
        if not self.queue:
            return -1
        num = self.queue.popleft()
        self.available.remove(num)
        return num
    def check(self, number: int) -> bool:
        return number in self.available
    def release(self, number: int) -> None:
        if number not in self.available:
            self.available.add(number)
            self.queue.append(number)

# Example usage:
dir = PhoneDirectory(3)
print(dir.get())    # Output: 0
print(dir.get())    # Output: 1
print(dir.check(2)) # Output: True
print(dir.get())    # Output: 2
print(dir.check(2)) # Output: False
print(dir.release(2))
print(dir.check(2)) # Output: True
