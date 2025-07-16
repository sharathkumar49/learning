"""
LeetCode 2211. Count Collisions on a Road

Given a string directions consisting of 'L', 'R', and 'S', return the total number of collisions that will happen on the road.

Example:
Input: directions = "RLRSLL"
Output: 5

Constraints:
- 1 <= directions.length <= 10^5
- directions[i] is 'L', 'R', or 'S'
"""

def countCollisions(directions):
    res = 0
    directions = list(directions)
    n = len(directions)
    for i in range(1, n):
        if directions[i-1] == 'R' and directions[i] == 'L':
            res += 2
            directions[i-1] = directions[i] = 'S'
        elif directions[i-1] == 'R' and directions[i] == 'S':
            res += 1
            directions[i-1] = 'S'
        elif directions[i-1] == 'S' and directions[i] == 'L':
            res += 1
            directions[i] = 'S'
    # Count remaining collisions for L and R
    for i in range(n):
        if directions[i] == 'L' and any(d != 'L' for d in directions[:i]):
            res += 1
        if directions[i] == 'R' and any(d != 'R' for d in directions[i+1:]):
            res += 1
    return res

# Example usage:
# print(countCollisions("RLRSLL"))  # Output: 5
