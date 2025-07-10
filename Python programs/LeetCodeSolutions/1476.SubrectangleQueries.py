"""
LeetCode 1476. Subrectangle Queries

Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers in the constructor and supports two methods:
- updateSubrectangle(row1, col1, row2, col2, newValue): Updates all values with newValue in the subrectangle.
- getValue(row, col): Returns the current value at (row, col).

Constraints:
- 1 <= rows, cols <= 100
- 1 <= newValue, rectangle[i][j] <= 10^9
- At most 500 operations will be performed.

Example:
Input: ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue"], [[[1,2,1],[4,3,4],[3,2,1],[1,1,1]],[0,2],[0,0,3,2,5],[0,2],[3,1]]
Output: [null,1,null,5,1]
"""
class SubrectangleQueries:
    def __init__(self, rectangle):
        self.rect = [row[:] for row in rectangle]

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.rect[i][j] = newValue

    def getValue(self, row, col):
        return self.rect[row][col]

# Example usage:
# rectangle = [[1,2,1],[4,3,4],[3,2,1],[1,1,1]]
# obj = SubrectangleQueries(rectangle)
# print(obj.getValue(0,2))  # Output: 1
# obj.updateSubrectangle(0,0,3,2,5)
# print(obj.getValue(0,2))  # Output: 5
