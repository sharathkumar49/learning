"""
LeetCode 1845. Seat Reservation Manager

Design a system that manages seat reservations in a theater. Implement the SeatManager class:
- SeatManager(int n): Initializes a SeatManager with n seats numbered from 1 to n.
- int reserve(): Reserves the smallest-numbered unreserved seat and returns its number.
- void unreserve(int seatNumber): Unreserves the seat with the given number.

Example 1:
Input: ["SeatManager","reserve","reserve","unreserve","reserve","reserve","reserve","reserve","unreserve"], [[5],[],[],[2],[],[],[],[],[5]]
Output: [null,1,2,null,2,3,4,5,null]

Constraints:
- 1 <= n <= 10^5
- 1 <= seatNumber <= n
- At most 10^5 calls in total will be made to reserve and unreserve.
"""

import heapq

class SeatManager:
    def __init__(self, n):
        self.available = list(range(1, n+1))
        heapq.heapify(self.available)
    def reserve(self):
        return heapq.heappop(self.available)
    def unreserve(self, seatNumber):
        heapq.heappush(self.available, seatNumber)

# Example usage:
# sm = SeatManager(5)
# print(sm.reserve())  # Output: 1
# print(sm.reserve())  # Output: 2
# sm.unreserve(2)
# print(sm.reserve())  # Output: 2
