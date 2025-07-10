"""
LeetCode 1496. Path Crossing

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', return true if the path crosses itself at any point, otherwise return false.

Constraints:
- 1 <= path.length <= 10^4
- path[i] is either 'N', 'S', 'E', or 'W'.

Example:
Input: path = "NES"
Output: False
"""
def isPathCrossing(path):
    x = y = 0
    visited = set([(0,0)])
    for d in path:
        if d == 'N': y += 1
        elif d == 'S': y -= 1
        elif d == 'E': x += 1
        else: x -= 1
        if (x, y) in visited:
            return True
        visited.add((x, y))
    return False

# Example usage:
path = "NES"
print(isPathCrossing(path))  # Output: False
