"""
1138. Alphabet Board Path

On an alphabet board, we start at position (0, 0), corresponding to character 'a'.
The board is a 5x5 grid, with the last row containing only 'z':

    a b c d e
    f g h i j
    k l m n o
    p q r s t
    u v w x y
    z

Given a string target, return a sequence of moves to spell out the string on the board. Each move is one of 'U', 'D', 'L', 'R' (up, down, left, right), or '!' to select the character. The path should be as short as possible.

Constraints:
- 1 <= target.length <= 100
- target consists only of English lowercase letters.

Example:
Input: target = "leet"
Output: "DDR!UURRR!!DDD!"

"""
def alphabetBoardPath(target):
    board = {
        c: (i // 5, i % 5)
        for i, c in enumerate('abcdefghijklmnopqrstuvwxyz')
    }
    res = []
    x, y = 0, 0
    for ch in target:
        nx, ny = board[ch]
        # Special handling for 'z' to avoid invalid moves
        if ch == 'z':
            # Move horizontally first, then vertically
            while y > ny:
                res.append('L')
                y -= 1
            while x < nx:
                res.append('D')
                x += 1
            while y < ny:
                res.append('R')
                y += 1
            while x > nx:
                res.append('U')
                x -= 1
        else:
            # Move vertically first, then horizontally
            while x > nx:
                res.append('U')
                x -= 1
            while y > ny:
                res.append('L')
                y -= 1
            while x < nx:
                res.append('D')
                x += 1
            while y < ny:
                res.append('R')
                y += 1
        res.append('!')
    return ''.join(res)

# Example usage
if __name__ == "__main__":
    print(alphabetBoardPath("leet"))  # Output: "DDR!UURRR!!DDD!"
