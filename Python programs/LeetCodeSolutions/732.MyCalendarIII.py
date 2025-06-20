"""
LeetCode 732. My Calendar III

Implement a MyCalendarThree class to book events. Each event is represented as a half-open interval [start, end), and you may assume that the event's start time is always less than the end time.

Implement the MyCalendarThree class:
- MyCalendarThree() Initializes the calendar object.
- int book(int start, int end) Returns the maximum number of events that have been booked concurrently so far.

Example 1:
Input
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, 1, 1, 2, 3, 3, 3]

Constraints:
- 0 <= start < end <= 10^9
- At most 400 calls will be made to book.
"""
from collections import Counter

class MyCalendarThree:
    def __init__(self):
        self.timeline = Counter()
    def book(self, start: int, end: int) -> int:
        self.timeline[start] += 1
        self.timeline[end] -= 1
        active = res = 0
        for t in sorted(self.timeline):
            active += self.timeline[t]
            res = max(res, active)
        return res

# Example usage
if __name__ == "__main__":
    cal = MyCalendarThree()
    print(cal.book(10, 20))  # Output: 1
    print(cal.book(50, 60))  # Output: 1
    print(cal.book(10, 40))  # Output: 2
    print(cal.book(5, 15))   # Output: 3
    print(cal.book(5, 10))   # Output: 3
    print(cal.book(25, 55))  # Output: 3
