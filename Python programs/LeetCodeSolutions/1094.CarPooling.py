"""
1094. Car Pooling

You are given a list of trips, where trips[i] = [num_passengers, from_i, to_i]. Return true if it is possible to pick up and drop off all passengers for all the given trips, given the capacity.

Constraints:
- 1 <= trips.length <= 1000
- 1 <= num_passengers <= 100
- 0 <= from_i < to_i <= 1000
- 1 <= capacity <= 10^5

Example:
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
"""
from typing import List

def carPooling(trips: List[List[int]], capacity: int) -> bool:
    stops = [0] * 1001
    for num, start, end in trips:
        stops[start] += num
        stops[end] -= num
    curr = 0
    for s in stops:
        curr += s
        if curr > capacity:
            return False
    return True

# Example usage:
trips = [[2,1,5],[3,3,7]]
capacity = 4
print(carPooling(trips, capacity))  # Output: False
