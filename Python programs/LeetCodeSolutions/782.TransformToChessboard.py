"""
782. Transform to Chessboard

You are given an n x n binary matrix board. In a single move, you can swap any two rows or any two columns. Return the minimum number of moves to transform the board into a chessboard, or -1 if impossible.

Example 1:
Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
Output: 2

Example 2:
Input: board = [[0,1],[1,0]]
Output: 0

Constraints:
- n == board.length
- n == board[i].length
- 2 <= n <= 30
- board[i][j] is 0 or 1.
"""
def movesToChessboard(board):
    n = len(board)
    import collections
    rows = [tuple(row) for row in board]
    cols = [tuple(col) for col in zip(*board)]
    for lines in (rows, cols):
        count = collections.Counter(lines)
        if len(count) != 2:
            return -1
        keys = list(count.keys())
        if abs(count[keys[0]] - count[keys[1]]) > 1:
            return -1
        for a, b in zip(keys[0], keys[1]):
            if a == b:
                return -1
    def min_swaps(lines):
        ones = sum(line[0] for line in lines)
        n = len(lines)
        if n % 2:
            if ones * 2 < n:
                start = 0
            else:
                start = 1
            return sum(line[0] != (i + start) % 2 for i, line in enumerate(lines)) // 2
        else:
            return min(sum(line[0] != i % 2 for i, line in enumerate(lines)),
                       sum(line[0] != (i + 1) % 2 for i, line in enumerate(lines))) // 2
    return min_swaps(rows) + min_swaps(cols)

# Example usage:
print(movesToChessboard([[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]))  # Output: 2
print(movesToChessboard([[0,1],[1,0]]))  # Output: 0
