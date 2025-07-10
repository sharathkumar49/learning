"""
LeetCode 1921. Eliminate Maximum Number of Monsters

Given two integer arrays dist and speed, return the maximum number of monsters you can eliminate before any of them reach the city.

Example:
Input: dist = [1,3,4], speed = [1,1,1]
Output: 3

Constraints:
- n == dist.length == speed.length
- 1 <= n <= 10^5
- 1 <= dist[i], speed[i] <= 10^5
"""

def eliminateMaximum(dist, speed):
    time = sorted([d/s for d, s in zip(dist, speed)])
    for i, t in enumerate(time):
        if t <= i:
            return i
    return len(dist)

# Example usage:
# print(eliminateMaximum([1,3,4], [1,1,1]))  # Output: 3
