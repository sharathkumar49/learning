"""
365. Water and Jug Problem

You are given two jugs with capacities jug1Capacity and jug2Capacity and an integer targetCapacity. Return true if it is possible to measure exactly targetCapacity liters using the two jugs.

Constraints:
- 1 <= jug1Capacity, jug2Capacity, targetCapacity <= 10^6
"""
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        from math import gcd
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0

# Example usage:
jug1Capacity = 3
jug2Capacity = 5
targetCapacity = 4
print(Solution().canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity))  # Output: True
