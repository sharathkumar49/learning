"""
LeetCode 2120. Execution of All Suffix Instructions Staying in a Grid

Given a grid of size n x n, a start position, and a string s of instructions, return an array where the i-th element is the number of instructions you can execute from the i-th suffix of s without leaving the grid.

Example:
Input: n = 3, startPos = [0,1], s = "RRDDLU"
Output: [1,5,4,3,1,0]

Constraints:
- 1 <= n <= 500
- s consists of 'L', 'R', 'U', 'D'
"""

def executeInstructions(n, startPos, s):
    res = []
    dirs = {'L': (0,-1), 'R': (0,1), 'U': (-1,0), 'D': (1,0)}
    for i in range(len(s)):
        x, y = startPos
        cnt = 0
        for j in range(i, len(s)):
            dx, dy = dirs[s[j]]
            x += dx
            y += dy
            if 0 <= x < n and 0 <= y < n:
                cnt += 1
            else:
                break
        res.append(cnt)
    return res

# Example usage:
# print(executeInstructions(3, [0,1], "RRDDLU"))  # Output: [1,5,4,3,1,0]
