"""
1109. Corporate Flight Bookings

There are n flights, and you are given bookings[i] = [first, last, seats]. Return an array answer of length n, where answer[i] is the total number of seats booked for flight i+1.

Constraints:
- 1 <= n <= 2 * 10^4
- 1 <= bookings.length <= 2 * 10^4
- 1 <= first <= last <= n
- 1 <= seats <= 10^4

Example:
Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
"""
from typing import List

def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    res = [0] * (n + 1)
    for first, last, seats in bookings:
        res[first - 1] += seats
        res[last] -= seats
    for i in range(1, n):
        res[i] += res[i - 1]
    return res[:-1]

# Example usage:
bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
print(corpFlightBookings(bookings, n))  # Output: [10, 55, 45, 25, 25]
