"""
353. Design Snake Game

Design a Snake game that is played on a device with screen size width x height. The snake is initially positioned at the top left corner (0, 0) with a length of 1 unit.

Implement the SnakeGame class:
- SnakeGame(int width, int height, int[][] food) Initializes the object with the screen size and the positions of the food.
- int move(String direction) Moves the snake in the given direction. Returns the game's score after the move. Returns -1 if the game is over.

Constraints:
- 1 <= width, height <= 10^4
- 1 <= food.length <= 1000
- food[i].length == 2
- 0 <= food[i][0] < height
- 0 <= food[i][1] < width
- direction is 'U', 'D', 'L', or 'R'.
- At most 10^4 calls will be made to move.
"""
from collections import deque

class SnakeGame:
    def __init__(self, width: int, height: int, food: list):
        self.width = width
        self.height = height
        self.food = food
        self.snake = deque([(0, 0)])
        self.snake_set = set([(0, 0)])
        self.score = 0
        self.dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    def move(self, direction: str) -> int:
        head = self.snake[0]
        dx, dy = self.dirs[direction]
        new_head = (head[0] + dx, head[1] + dy)
        if (not (0 <= new_head[0] < self.height and 0 <= new_head[1] < self.width)) or (new_head in self.snake_set and new_head != self.snake[-1]):
            return -1
        if self.food and list(new_head) == self.food[0]:
            self.food.pop(0)
            self.score += 1
        else:
            tail = self.snake.pop()
            self.snake_set.remove(tail)
        self.snake.appendleft(new_head)
        self.snake_set.add(new_head)
        return self.score

# Example usage:
game = SnakeGame(3, 2, [[1,2],[0,1]])
print(game.move("R"))  # Output: 0
print(game.move("D"))  # Output: 0
print(game.move("R"))  # Output: 1
print(game.move("U"))  # Output: 1
print(game.move("L"))  # Output: 2
print(game.move("U"))  # Output: -1
