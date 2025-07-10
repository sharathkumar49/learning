"""
LeetCode 2126. Destroying Asteroids

Given an integer mass and an array asteroids, return true if you can destroy all asteroids.

Example:
Input: mass = 10, asteroids = [3,9,19,5,21]
Output: true

Constraints:
- 1 <= mass <= 10^5
- 1 <= asteroids.length <= 10^5
- 1 <= asteroids[i] <= 10^5
"""

def asteroidsDestroyed(mass, asteroids):
    asteroids.sort()
    for a in asteroids:
        if mass < a:
            return False
        mass += a
    return True

# Example usage:
# print(asteroidsDestroyed(10, [3,9,19,5,21]))  # Output: True
