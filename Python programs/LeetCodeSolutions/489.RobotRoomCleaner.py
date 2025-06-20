"""
489. Robot Room Cleaner

Given a robot in a room modeled as a grid, implement the robot's cleaning algorithm. The robot has an API with the following functions:
- move(): returns true if the cell in front is open and robot moves into the cell.
- turnLeft(): robot will stay in the same cell after calling turnLeft/turnRight.
- turnRight(): robot will stay in the same cell after calling turnLeft/turnRight.
- clean(): cleans the current cell.

Note: The robot's API is not implemented here. In a real interview, you would be provided with a robot object.

Constraints:
- The number of cells in the room is in the range [1, 1000].
- The number of times the robot will be called is in the range [1, 1000].

Example:
Input: room = [[1,1,1],[1,1,1],[0,1,1]], row = 1, col = 3, direction = 0
Output: Robot cleaned all accessible cells.
"""

# The Robot API is not implemented here. This is a template for the solution.
class Solution:
    def cleanRoom(self, robot):
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        visited = set()
        def go(x, y, d):
            robot.clean()
            visited.add((x, y))
            for i in range(4):
                nd = (d + i) % 4
                nx, ny = x + directions[nd][0], y + directions[nd][1]
                if (nx, ny) not in visited and robot.move():
                    go(nx, ny, nd)
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnLeft()
                    robot.turnLeft()
                robot.turnRight()
        go(0, 0, 0)

# Example usage:
# Not executable without the Robot API implementation.
