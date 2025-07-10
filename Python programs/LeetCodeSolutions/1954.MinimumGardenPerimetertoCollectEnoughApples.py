"""
LeetCode 1954. Minimum Garden Perimeter to Collect Enough Apples

Given an integer neededApples, return the minimum perimeter of a garden to collect at least neededApples apples.

Example:
Input: neededApples = 1
Output: 8

Constraints:
- 1 <= neededApples <= 10^15
"""

def minimumPerimeter(neededApples):
    n = 0
    while 2*n*(n+1)*(2*n+1) < neededApples:
        n += 1
    return 8*n

# Example usage:
# print(minimumPerimeter(1))  # Output: 8
