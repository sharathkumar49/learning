"""
836. Rectangle Overlap

Given two rectangles, return true if they overlap. Each rectangle is represented as [x1, y1, x2, y2].

Example 1:
Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true

Example 2:
Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false

Constraints:
- rec1.length == 4
- rec2.length == 4
- -10^9 <= rec1[i], rec2[i] <= 10^9
- rec1 and rec2 represent a valid rectangle.
"""
def isRectangleOverlap(rec1, rec2):
    return not (rec1[2] <= rec2[0] or rec2[2] <= rec1[0] or rec1[3] <= rec2[1] or rec2[3] <= rec1[1])

# Example usage:
print(isRectangleOverlap([0,0,2,2], [1,1,3,3]))  # Output: True
print(isRectangleOverlap([0,0,1,1], [1,0,2,1]))  # Output: False
