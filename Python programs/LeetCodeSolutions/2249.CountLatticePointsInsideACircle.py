"""
LeetCode 2249. Count Lattice Points Inside a Circle

Given circles, return the number of lattice points inside at least one circle.

Example:
Input: circles = [[2,2,1],[3,4,1]]
Output: 7

Constraints:
- 1 <= circles.length <= 200
- 1 <= x, y, r <= 200
"""

def countLatticePoints(circles):
    points = set()
    for x, y, r in circles:
        for i in range(x-r, x+r+1):
            for j in range(y-r, y+r+1):
                if (i-x)**2 + (j-y)**2 <= r*r:
                    points.add((i,j))
    return len(points)

# Example usage:
# print(countLatticePoints([[2,2,1],[3,4,1]]))  # Output: 7
