"""
LeetCode 731. My Calendar II

Implement a MyCalendarTwo class to book events. Each event is represented as a half-open interval [start, end), and you may assume that the event's start time is always less than the end time.

Implement the MyCalendarTwo class:
- MyCalendarTwo() Initializes the calendar object.
- boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false.

Example 1:
Input
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, true, true, true, false, true, true]

Constraints:
- 0 <= start < end <= 10^9
- At most 1000 calls will be made to book.
"""
class MyCalendarTwo:
    def __init__(self):
        self.booked = []
        self.overlaps = []
    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlaps:
            if max(s, start) < min(e, end):
                return False
        for s, e in self.booked:
            if max(s, start) < min(e, end):
                self.overlaps.append((max(s, start), min(e, end)))
        self.booked.append((start, end))
        return True

# Example usage
if __name__ == "__main__":
    cal = MyCalendarTwo()
    print(cal.book(10, 20))  # Output: True
    print(cal.book(50, 60))  # Output: True
    print(cal.book(10, 40))  # Output: True
    print(cal.book(5, 15))   # Output: False
    print(cal.book(5, 10))   # Output: True
    print(cal.book(25, 55))  # Output: True
