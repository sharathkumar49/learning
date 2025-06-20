"""
849. Maximize Distance to Closest Person

You are given an array seats where seats[i] = 1 means occupied and seats[i] = 0 means empty. Return the maximum distance to the closest person.

Example 1:
Input: seats = [1,0,0,0,1,0,1]
Output: 2

Example 2:
Input: seats = [1,0,0,0]
Output: 3

Constraints:
- 2 <= seats.length <= 2 * 10^4
- seats[i] is 0 or 1.
"""
def maxDistToClosest(seats):
    n = len(seats)
    prev = -1
    max_dist = 0
    for i, seat in enumerate(seats):
        if seat:
            if prev == -1:
                max_dist = i
            else:
                max_dist = max(max_dist, (i - prev) // 2)
            prev = i
    max_dist = max(max_dist, n - 1 - prev)
    return max_dist

# Example usage:
print(maxDistToClosest([1,0,0,0,1,0,1]))  # Output: 2
print(maxDistToClosest([1,0,0,0]))        # Output: 3
