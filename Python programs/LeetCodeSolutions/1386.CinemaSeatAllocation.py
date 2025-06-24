"""
LeetCode 1386. Cinema Seat Allocation

A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

Given the array reservedSeats containing the numbers of seats already reserved, return the maximum number of four-person groups you can assign on the cinema.

Constraints:
- 1 <= n <= 10^9
- 1 <= reservedSeats.length <= min(10*n, 10^4)
- reservedSeats[i].length == 2
- 1 <= reservedSeats[i][0] <= n
- 1 <= reservedSeats[i][1] <= 10

Example:
Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
"""
def maxNumberOfFamilies(n, reservedSeats):
    from collections import defaultdict
    reserved = defaultdict(set)
    for row, seat in reservedSeats:
        reserved[row].add(seat)
    result = 2 * n
    for row in reserved:
        count = 0
        if not (2 in reserved[row] or 3 in reserved[row] or 4 in reserved[row] or 5 in reserved[row]):
            count += 1
        if not (6 in reserved[row] or 7 in reserved[row] or 8 in reserved[row] or 9 in reserved[row]):
            count += 1
        if count == 0 and not (4 in reserved[row] or 5 in reserved[row] or 6 in reserved[row] or 7 in reserved[row]):
            count = 1
        result -= (2 - count)
    return result

# Example usage:
n = 3
reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
print(maxNumberOfFamilies(n, reservedSeats))  # Output: 4
