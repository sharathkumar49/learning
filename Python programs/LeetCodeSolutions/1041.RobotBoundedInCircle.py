"""
1041. Robot Bounded In Circle

On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive a sequence of instructions: 'G' (go straight 1 unit), 'L' (turn left 90 degrees), or 'R' (turn right 90 degrees). Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Constraints:
- 1 <= instructions.length <= 100
- instructions[i] is 'G', 'L', or 'R'.

Example:
Input: instructions = "GGLLGG"
Output: true
"""
def isRobotBounded(instructions: str) -> bool:
    x = y = 0
    dx, dy = 0, 1
    for ch in instructions:
        if ch == 'G':
            x += dx
            y += dy
        elif ch == 'L':
            dx, dy = -dy, dx
        else:
            dx, dy = dy, -dx
    return (x, y) == (0, 0) or (dx, dy) != (0, 1)

# Example usage:
instructions = "GGLLGG"
print(isRobotBounded(instructions))  # Output: True
