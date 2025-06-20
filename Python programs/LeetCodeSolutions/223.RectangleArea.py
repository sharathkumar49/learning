"""
223. Rectangle Area
https://leetcode.com/problems/rectangle-area/

Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and top-right corner (ax2, ay2).
The second rectangle is defined by its bottom-left corner (bx1, by1) and top-right corner (bx2, by2).

Constraints:
- -10^4 <= ax1 <= ax2 <= 10^4
- -10^4 <= ay1 <= ay2 <= 10^4
- -10^4 <= bx1 <= bx2 <= 10^4
- -10^4 <= by1 <= by2 <= 10^4

Example 1:
Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45

Example 2:
Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
Output: 16
"""
def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)
    overlap_x = max(0, min(ax2, bx2) - max(ax1, bx1))
    overlap_y = max(0, min(ay2, by2) - max(ay1, by1))
    overlap = overlap_x * overlap_y
    return area1 + area2 - overlap

# Example usage:
if __name__ == "__main__":
    print(computeArea(-3,0,3,4,0,-1,9,2))  # Output: 45
    print(computeArea(-2,-2,2,2,-2,-2,2,2)) # Output: 16
