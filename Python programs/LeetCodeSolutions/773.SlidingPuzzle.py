"""
773. Sliding Puzzle

On a 2x3 board, there are 5 tiles labeled 1 to 5, and an empty square represented by 0. A move consists of swapping 0 with an adjacent number. The goal is to return the minimum number of moves to reach the solved state [[1,2,3],[4,5,0]], or -1 if unsolvable.

Example 1:
Input: board = [[1,2,3],[4,0,5]]
Output: 1

Example 2:
Input: board = [[1,2,3],[5,4,0]]
Output: -1

Constraints:
- board.length == 2
- board[i].length == 3
- 0 <= board[i][j] <= 5
- Each value board[i][j] is unique.
"""
from collections import deque

def slidingPuzzle(board):
    start = ''.join(str(num) for row in board for num in row)
    target = '123450'
    neighbors = {
        0: [1,3], 1: [0,2,4], 2: [1,5],
        3: [0,4], 4: [1,3,5], 5: [2,4]
    }
    queue = deque([(start, 0)])
    visited = set([start])
    while queue:
        state, moves = queue.popleft()
        if state == target:
            return moves
        zero = state.index('0')
        for nei in neighbors[zero]:
            lst = list(state)
            lst[zero], lst[nei] = lst[nei], lst[zero]
            new_state = ''.join(lst)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, moves+1))
    return -1

# Example usage:
print(slidingPuzzle([[1,2,3],[4,0,5]]))  # Output: 1
print(slidingPuzzle([[1,2,3],[5,4,0]]))  # Output: -1
