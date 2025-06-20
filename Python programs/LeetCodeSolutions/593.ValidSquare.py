"""
593. Valid Square
Difficulty: Medium

Given the coordinates of four points in 2D space, return true if the four points construct a square.

Example 1:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true

Example 2:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false

Constraints:
All the input integers are in the range [-10000, 10000].
All the input integers are unique.
"""

def validSquare(p1, p2, p3, p4):
    def dist(a, b):
        return (a[0]-b[0])**2 + (a[1]-b[1])**2
    points = [p1, p2, p3, p4]
    dists = sorted([dist(points[i], points[j]) for i in range(4) for j in range(i+1, 4)])
    return dists[0] > 0 and dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5]

# Example usage
if __name__ == "__main__":
    print(validSquare([0,0],[1,1],[1,0],[0,1]))  # Output: True
    print(validSquare([0,0],[1,1],[1,0],[0,12])) # Output: False
