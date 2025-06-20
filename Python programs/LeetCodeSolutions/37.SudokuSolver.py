# 37. Sudoku Solver
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# Example 1:
# Input: board = [
#   ["5","3",".",".","7",".",".",".","."]
#   ,["6",".",".","1","9","5",".",".","."]
#   ,[".","9","8",".",".",".",".","6","."]
#   ,["8",".",".",".","6",".",".",".","3"]
#   ,["4",".",".","8",".","3",".",".","1"]
#   ,["7",".",".",".","2",".",".",".","6"]
#   ,[".","6",".",".",".",".","2","8","."]
#   ,[".",".",".","4","1","9",".",".","5"]
#   ,[".",".",".",".","8",".",".","7","9"]
# ]
# Output: The board is solved in-place.
#
# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.
# It is guaranteed that the input board has only one solution.

def solveSudoku(board):
    def is_valid(r, c, k):
        for i in range(9):
            if board[i][c] == k or board[r][i] == k or board[3*(r//3)+i//3][3*(c//3)+i%3] == k:
                return False
        return True
    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in map(str, range(1, 10)):
                        if is_valid(i, j, k):
                            board[i][j] = k
                            if backtrack():
                                return True
                            board[i][j] = '.'
                    return False
        return True
    backtrack()

# Example usage
board = [
    ["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
]
solveSudoku(board)
print("Solved Sudoku:")
for row in board:
    print(row)
