"""
LeetCode 1274. Number of Ships in a Rectangle

(This problem requires an external API `Sea.hasShips` which is not implemented here. The code below is a template for LeetCode submission.)

Given two points that represent the top right and bottom left corners of a rectangle, return the number of ships in that rectangle. You can only use the Sea.hasShips API.

Constraints:
- The rectangle boundaries are within [0, 999].
- The number of ships is at most 10.

Example:
Input: topRight = [2,3], bottomLeft = [0,0]
Output: (depends on Sea.hasShips)
"""
# The Sea API is not implemented here. This is a template for LeetCode submission.
def countShips(sea, topRight, bottomLeft):
    x0, y0 = bottomLeft
    x1, y1 = topRight
    if x0 > x1 or y0 > y1 or not sea.hasShips(topRight, bottomLeft):
        return 0
    if x0 == x1 and y0 == y1:
        return 1
    mx, my = (x0 + x1) // 2, (y0 + y1) // 2
    return (countShips(sea, [mx, my], [x0, y0]) +
            countShips(sea, [x1, my], [mx+1, y0]) +
            countShips(sea, [mx, y1], [x0, my+1]) +
            countShips(sea, [x1, y1], [mx+1, my+1]))

# Example usage:
# Not executable here as Sea API is not implemented.
