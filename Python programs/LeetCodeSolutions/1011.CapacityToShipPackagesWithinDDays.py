"""
1011. Capacity To Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another within D days.
The i-th package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

Constraints:
- 1 <= D <= weights.length <= 50000
- 1 <= weights[i] <= 500

Example:
Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all packages in 5 days.
"""
from typing import List

def shipWithinDays(weights: List[int], D: int) -> int:
    def can_ship(cap):
        days = 1
        total = 0
        for w in weights:
            if total + w > cap:
                days += 1
                total = 0
            total += w
        return days <= D
    left, right = max(weights), sum(weights)
    while left < right:
        mid = (left + right) // 2
        if can_ship(mid):
            right = mid
        else:
            left = mid + 1
    return left

# Example usage:
weights = [1,2,3,4,5,6,7,8,9,10]
D = 5
print(shipWithinDays(weights, D))  # Output: 15
