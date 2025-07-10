"""
LeetCode 2069. Walking Robot Simulation II

Design a robot that walks in a grid and can report its position and facing direction.

Example:
Input: ["Robot","step","getPos","getDir"], [[6,3],[2],[],[]]
Output: [null,null,[2,0],"East"]

Constraints:
- 2 <= width, height <= 100
- 1 <= num of operations <= 100
"""

class Robot:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.dir = 0
        self.dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        self.names = ["East","North","West","South"]
        self.perimeter = 2*(width+height)-4
    def step(self, num):
        num %= self.perimeter
        for _ in range(num):
            nx, ny = self.x + self.dirs[self.dir][0], self.y + self.dirs[self.dir][1]
            if 0 <= nx < self.width and 0 <= ny < self.height:
                self.x, self.y = nx, ny
            else:
                self.dir = (self.dir + 1) % 4
                self.x += self.dirs[self.dir][0]
                self.y += self.dirs[self.dir][1]
    def getPos(self):
        return [self.x, self.y]
    def getDir(self):
        return self.names[self.dir]

# Example usage:
# robot = Robot(6,3)
# robot.step(2)
# print(robot.getPos())  # Output: [2,0]
# print(robot.getDir())  # Output: "East"
