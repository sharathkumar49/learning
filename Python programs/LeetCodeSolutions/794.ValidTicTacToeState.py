"""
794. Valid Tic-Tac-Toe State

Given a Tic-Tac-Toe board as a string array board, return true if and only if it is possible to reach this board position during a valid game.

Example 1:
Input: board = ["O  ","   ","   "]
Output: false

Example 2:
Input: board = ["XOX"," X ","   "]
Output: false

Example 3:
Input: board = ["XOX","O O","XOX"]
Output: true

Constraints:
- board.length == 3
- board[i].length == 3
- board[i][j] is 'X', 'O', or ' '.
"""
def validTicTacToe(board):
    x = sum(row.count('X') for row in board)
    o = sum(row.count('O') for row in board)
    def win(p):
        for i in range(3):
            if all(board[i][j] == p for j in range(3)) or all(board[j][i] == p for j in range(3)):
                return True
        if all(board[i][i] == p for i in range(3)) or all(board[i][2-i] == p for i in range(3)):
            return True
        return False
    if o > x or x - o > 1:
        return False
    if win('X') and x != o + 1:
        return False
    if win('O') and x != o:
        return False
    return True

# Example usage:
print(validTicTacToe(["O  ","   ","   "]))  # Output: False
print(validTicTacToe(["XOX"," X ","   "]))  # Output: False
print(validTicTacToe(["XOX","O O","XOX"]))  # Output: True
