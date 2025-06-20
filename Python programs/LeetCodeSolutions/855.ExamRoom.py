"""
855. Exam Room

There is an exam room with n seats in a single row. When a student enters, they sit at the seat that maximizes the distance to the closest person. If there are multiple such seats, they sit at the lowest-numbered seat. Implement the ExamRoom class with seat() and leave(p) methods.

Example 1:
Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]

Constraints:
- 1 <= n <= 10^9
- At most 10^4 calls to seat() and leave().
"""
import bisect
class ExamRoom:
    def __init__(self, n):
        self.n = n
        self.seats = []
    def seat(self):
        if not self.seats:
            self.seats.append(0)
            return 0
        max_dist = self.seats[0]
        pos = 0
        for i in range(1, len(self.seats)):
            d = (self.seats[i] - self.seats[i-1]) // 2
            if d > max_dist:
                max_dist = d
                pos = self.seats[i-1] + d
        if self.n - 1 - self.seats[-1] > max_dist:
            pos = self.n - 1
        bisect.insort(self.seats, pos)
        return pos
    def leave(self, p):
        self.seats.remove(p)

# Example usage:
room = ExamRoom(10)
print(room.seat())  # Output: 0
print(room.seat())  # Output: 9
print(room.seat())  # Output: 4
print(room.seat())  # Output: 2
room.leave(4)
print(room.seat())  # Output: 5
