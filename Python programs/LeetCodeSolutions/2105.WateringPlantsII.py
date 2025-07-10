"""
LeetCode 2105. Watering Plants II

Given an array plants and two capacities, return the number of times Alice and Bob have to refill to water all plants.

Example:
Input: plants = [2,2,3,3], capacityA = 5, capacityB = 5
Output: 2

Constraints:
- 1 <= plants.length <= 10^5
- 1 <= capacityA, capacityB <= 10^9
- 1 <= plants[i] <= max(capacityA, capacityB)
"""

def minimumRefill(plants, capacityA, capacityB):
    n = len(plants)
    a, b = 0, n-1
    ca, cb = capacityA, capacityB
    res = 0
    while a <= b:
        if a == b:
            if ca >= plants[a] or cb >= plants[b]:
                break
            res += 1
            break
        if ca < plants[a]:
            ca = capacityA
            res += 1
        ca -= plants[a]
        a += 1
        if cb < plants[b]:
            cb = capacityB
            res += 1
        cb -= plants[b]
        b -= 1
    return res

# Example usage:
# print(minimumRefill([2,2,3,3], 5, 5))  # Output: 2
