# Tic-Tac-Toe Game (Console-based)

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current = 'X'
    while True:
        print_board(board)
        move = input(f"Player {current}, enter row and column (0-2, space separated): ").split()
        if len(move) != 2 or not all(m.isdigit() for m in move):
            print("Invalid input. Try again.")
            continue
        r, c = map(int, move)
        if not (0 <= r < 3 and 0 <= c < 3) or board[r][c] != ' ':
            print("Invalid move. Try again.")
            continue
        board[r][c] = current
        if check_win(board, current):
            print_board(board)
            print(f"Player {current} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        current = 'O' if current == 'X' else 'X'

if __name__ == "__main__":
    main()
