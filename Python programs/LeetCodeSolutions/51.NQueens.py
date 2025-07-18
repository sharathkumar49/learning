# 51. N-Queens
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
#
# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#
# Example 2:
# Input: n = 1
# Output: [["Q"]]
#
# Constraints:
# 1 <= n <= 9

def solveNQueens(n):
    res = []
    board = ["." * n for _ in range(n)]
    cols = set()
    diag1 = set()
    diag2 = set()
    def backtrack(r):
        if r == n:
            res.append(board[:])
            return
        for c in range(n):
            if c in cols or (r-c) in diag1 or (r+c) in diag2:
                continue
            board[r] = board[r][:c] + "Q" + board[r][c+1:]
            cols.add(c)
            diag1.add(r-c)
            diag2.add(r+c)
            backtrack(r+1)
            board[r] = board[r][:c] + "." + board[r][c+1:]
            cols.remove(c)
            diag1.remove(r-c)
            diag2.remove(r+c)
    backtrack(0)
    return res

# Example usage
n = 4
print("N-Queens solutions:", solveNQueens(n))
