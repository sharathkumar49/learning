"""
LeetCode 2582. Pass the Pillow

Given n people and time t, return the person who has the pillow after t seconds.

Constraints:
- 2 <= n <= 1000
- 0 <= t <= 10^9
"""

def passThePillow(n, t):
    cycle = n-1
    t %= 2*cycle
    if t < cycle:
        return t+1
    else:
        return 2*cycle-t+1
# Example usage:
# print(passThePillow(4, 5))  # Output: 2
