"""
LeetCode 1637. Widest Vertical Area Between Two Points Containing No Points

Given n points on a 2D plane, return the widest vertical area between two points such that no points are inside the area.

Example 1:
Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1

Constraints:
- 2 <= n <= 10^5
- points[i].length == 2
- 0 <= points[i][j] <= 10^9
"""

def maxWidthOfVerticalArea(points):
    xs = sorted(x for x, y in points)
    return max(xs[i+1] - xs[i] for i in range(len(xs)-1))

# Example usage:
# points = [[8,7],[9,9],[7,4],[9,7]]
# print(maxWidthOfVerticalArea(points))  # Output: 1
