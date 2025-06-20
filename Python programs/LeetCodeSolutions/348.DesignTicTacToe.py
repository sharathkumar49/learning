"""
348. Design Tic-Tac-Toe

Design a Tic-tac-toe game that is played between two players on a n x n grid.

Implement the TicTacToe class:
- TicTacToe(int n) Initializes the object the size of the board n.
- int move(int row, int col, int player) Indicates that player with id player makes a move at the cell (row, col). The move is guaranteed to be a valid move.

Constraints:
- 2 <= n <= 100
- player is 1 or 2
- 0 <= row, col < n
- At most n^2 calls will be made to move.
"""
class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0
    def move(self, row: int, col: int, player: int) -> int:
        add = 1 if player == 1 else -1
        self.rows[row] += add
        self.cols[col] += add
        if row == col:
            self.diag += add
        if row + col == self.n - 1:
            self.anti_diag += add
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diag) == self.n or abs(self.anti_diag) == self.n:
            return player
        return 0

# Example usage:
ttt = TicTacToe(3)
print(ttt.move(0, 0, 1))  # Output: 0
print(ttt.move(0, 2, 2))  # Output: 0
print(ttt.move(2, 2, 1))  # Output: 0
print(ttt.move(1, 1, 2))  # Output: 0
print(ttt.move(2, 0, 1))  # Output: 0
print(ttt.move(1, 0, 2))  # Output: 0
print(ttt.move(2, 1, 1))  # Output: 1
