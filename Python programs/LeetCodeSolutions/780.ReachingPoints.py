"""
780. Reaching Points

Given four integers sx, sy, tx, ty, return true if it is possible to convert the point (sx, sy) to (tx, ty) by repeatedly performing the following operation: either (x, y) -> (x + y, y) or (x, y) -> (x, x + y).

Example 1:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: true

Example 2:
Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: false

Constraints:
- 1 <= sx, sy, tx, ty <= 10^9
"""
def reachingPoints(sx, sy, tx, ty):
    while tx > sx and ty > sy:
        if tx > ty:
            tx %= ty
        else:
            ty %= tx
    return (tx == sx and ty >= sy and (ty - sy) % sx == 0) or (ty == sy and tx >= sx and (tx - sx) % sy == 0)

# Example usage:
print(reachingPoints(1, 1, 3, 5))  # Output: True
print(reachingPoints(1, 1, 2, 2))  # Output: False
