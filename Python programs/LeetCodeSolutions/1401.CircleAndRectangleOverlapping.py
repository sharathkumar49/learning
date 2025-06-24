"""
LeetCode 1401. Circle and Rectangle Overlapping

Given a circle represented as (x_center, y_center, radius) and an axis-aligned rectangle represented as (x1, y1, x2, y2), return true if the circle and rectangle overlap, otherwise return false.

Constraints:
- -10^7 <= x_center, y_center <= 10^7
- 0 < radius <= 10^7
- -10^7 <= x1 < x2 <= 10^7
- -10^7 <= y1 < y2 <= 10^7

Example:
Input: x_center = 1, y_center = 1, radius = 1, x1 = 0, y1 = 0, x2 = 2, y2 = 2
Output: true
"""
def checkOverlap(radius, x_center, y_center, x1, y1, x2, y2):
    x_closest = max(x1, min(x_center, x2))
    y_closest = max(y1, min(y_center, y2))
    dx = x_closest - x_center
    dy = y_closest - y_center
    return dx*dx + dy*dy <= radius*radius

# Example usage:
print(checkOverlap(1, 1, 1, 0, 0, 2, 2))  # Output: True
