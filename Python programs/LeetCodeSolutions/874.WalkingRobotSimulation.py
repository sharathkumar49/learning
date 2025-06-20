"""
874. Walking Robot Simulation

A robot moves on a 2D plane. Given a sequence of commands and obstacles, return the maximum Euclidean distance squared from the origin the robot can reach.

Example 1:
Input: commands = [4,-1,3], obstacles = []
Output: 25

Example 2:
Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65

Constraints:
- 1 <= commands.length <= 10^4
- commands[i] is -2, -1, or an integer in [1,9]
- 0 <= obstacles.length <= 10^4
- obstacles[i].length == 2
- -3 * 10^4 <= obstacles[i][j] <= 3 * 10^4
"""
def robotSim(commands, obstacles):
    obs = set(map(tuple, obstacles))
    x = y = d = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    res = 0
    for cmd in commands:
        if cmd == -2:
            d = (d + 3) % 4
        elif cmd == -1:
            d = (d + 1) % 4
        else:
            for _ in range(cmd):
                if (x+dx[d], y+dy[d]) not in obs:
                    x += dx[d]
                    y += dy[d]
                    res = max(res, x*x + y*y)
                else:
                    break
    return res

# Example usage:
print(robotSim([4,-1,3], []))  # Output: 25
print(robotSim([4,-1,4,-2,4], [[2,4]]))  # Output: 65
