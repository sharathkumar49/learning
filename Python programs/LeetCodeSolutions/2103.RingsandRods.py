"""
LeetCode 2103. Rings and Rods

Given a string rings, return the number of rods that have all three colors.

Example:
Input: rings = "B0R0G0R9G9B9"
Output: 1

Constraints:
- rings.length == 2 * n
- 1 <= n <= 100
- rings consists of 'R', 'G', 'B' and digits.
"""

def countPoints(rings):
    rods = [set() for _ in range(10)]
    for i in range(0, len(rings), 2):
        rods[int(rings[i+1])].add(rings[i])
    return sum(len(rod) == 3 for rod in rods)

# Example usage:
# print(countPoints("B0R0G0R9G9B9"))  # Output: 1
