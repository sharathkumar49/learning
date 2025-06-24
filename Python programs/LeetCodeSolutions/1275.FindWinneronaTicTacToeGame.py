"""
LeetCode 1275. Find Winner on a Tic Tac Toe Game

Given a 3x3 board, return the winner ('A' or 'B'), 'Draw', or 'Pending' if the game is not finished.

Constraints:
- moves.length <= 9
- moves[i].length == 2
- 0 <= moves[i][j] <= 2

Example:
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
"""
def tictactoe(moves):
    board = [[0]*3 for _ in range(3)]
    for i, (x, y) in enumerate(moves):
        board[x][y] = 1 if i % 2 == 0 else 2
    for i in range(3):
        if board[i][0] and board[i][0] == board[i][1] == board[i][2]:
            return 'A' if board[i][0] == 1 else 'B'
        if board[0][i] and board[0][i] == board[1][i] == board[2][i]:
            return 'A' if board[0][i] == 1 else 'B'
    if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
        return 'A' if board[0][0] == 1 else 'B'
    if board[0][2] and board[0][2] == board[1][1] == board[2][0]:
        return 'A' if board[0][2] == 1 else 'B'
    return 'Draw' if len(moves) == 9 else 'Pending'

# Example usage:
moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
print(tictactoe(moves))  # Output: "A"
