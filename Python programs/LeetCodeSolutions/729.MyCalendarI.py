"""
LeetCode 729. My Calendar I

Implement a MyCalendar class to book events. Each event is represented as a half-open interval [start, end), and you may assume that the event's start time is always less than the end time.

Implement the MyCalendar class:
- MyCalendar() Initializes the calendar object.
- boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false.

Example 1:
Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Constraints:
- 0 <= start < end <= 10^9
- At most 1000 calls will be made to book.
"""
class MyCalendar:
    def __init__(self):
        self.bookings = []
    def book(self, start: int, end: int) -> bool:
        for s, e in self.bookings:
            if max(s, start) < min(e, end):
                return False
        self.bookings.append((start, end))
        return True

# Example usage
if __name__ == "__main__":
    cal = MyCalendar()
    print(cal.book(10, 20))  # Output: True
    print(cal.book(15, 25))  # Output: False
    print(cal.book(20, 30))  # Output: True
