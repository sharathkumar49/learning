"""
LeetCode 2079. Watering Plants

Given an array plants and an integer capacity, return the number of steps required to water all plants.

Example:
Input: plants = [2,2,3,3], capacity = 5
Output: 14

Constraints:
- 1 <= plants.length <= 1000
- 1 <= capacity <= 10^9
- 1 <= plants[i] <= capacity
"""

def wateringPlants(plants, capacity):
    res = 0
    curr = capacity
    for i, w in enumerate(plants):
        if curr < w:
            res += 2*i
            curr = capacity
        curr -= w
        res += 1
    return res

# Example usage:
print(wateringPlants([2,2,3,3], 5))  # Output: 14
