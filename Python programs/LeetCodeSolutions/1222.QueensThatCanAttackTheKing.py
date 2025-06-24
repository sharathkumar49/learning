"""
1222. Queens That Can Attack the King

Given a chessboard with queens and a king, return all the queens that can attack the king.

Constraints:
- 1 <= queens.length <= 8
- queens[i].length == 2
- 0 <= queens[i][j] < 8
- king.length == 2

Example:
Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
Output: [[0,1],[1,0],[3,3]]

"""
def queensAttacktheKing(queens, king):
    board = [[0]*8 for _ in range(8)]
    for x, y in queens:
        board[x][y] = 1
    res = []
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
        x, y = king
        while 0 <= x+dx < 8 and 0 <= y+dy < 8:
            x += dx
            y += dy
            if board[x][y]:
                res.append([x, y])
                break
    return res

# Example usage
if __name__ == "__main__":
    queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
    king = [0,0]
    print(queensAttacktheKing(queens, king))  # Output: [[0,1],[1,0],[3,3]]
