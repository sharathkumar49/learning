"""
LeetCode 2037. Minimum Number of Moves to Seat Everyone

Given two arrays seats and students, return the minimum number of moves required to seat everyone.

Example:
Input: seats = [3,1,5], students = [2,7,4]
Output: 4

Constraints:
- n == seats.length == students.length
- 1 <= n <= 100
- 1 <= seats[i], students[i] <= 100
"""

def minMovesToSeat(seats, students):
    seats.sort()
    students.sort()
    return sum(abs(a-b) for a, b in zip(seats, students))

# Example usage:
# print(minMovesToSeat([3,1,5], [2,7,4]))  # Output: 4
