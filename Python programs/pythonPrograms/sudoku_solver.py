# Sudoku Solver (Backtracking Algorithm)
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def is_valid(board, num, pos):
    row, col = pos
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False
    box_x, box_y = col // 3, row // 3
    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0
    return False

if __name__ == "__main__":
    board = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]
    print("Original board:")
    print_board(board)
    if solve(board):
        print("\nSolved board:")
        print_board(board)
    else:
        print("No solution exists.")
