"""
LeetCode 1861. Rotating the Box

You are given an m x n matrix representing a box, where each cell is one of: '#' (stone), '*' (obstacle), or '.' (empty space). The box is rotated 90 degrees clockwise, and stones fall down due to gravity. Return the state of the box after rotation.

Example:
Input: box = [["#",".","#"]]
Output: [[".","#","#"]]

Constraints:
- m == box.length
- n == box[i].length
- 1 <= m, n <= 500
- box[i][j] is either '#', '*', or '.'
"""

def rotateTheBox(box):
    m, n = len(box), len(box[0])
    for row in box:
        empty = n - 1
        for j in range(n - 1, -1, -1):
            if row[j] == '*':
                empty = j - 1
            elif row[j] == '#':
                if j != empty:
                    row[empty], row[j] = row[j], '.'
                empty -= 1
    rotated = [[box[i][j] for i in range(m - 1, -1, -1)] for j in range(n)]
    return rotated

# Example usage:
box = [["#", ".", "#"]]
print(rotateTheBox(box))  # Output: [['.', '#', '#']]
