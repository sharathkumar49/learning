# Maze Generator and Solver
import random

def generate_maze(n, m):
    maze = [[1 for _ in range(m)] for _ in range(n)]
    def carve(x, y):
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x+dx*2, y+dy*2
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[x+dx][y+dy] = 0
                maze[nx][ny] = 0
                carve(nx, ny)
    maze[1][1] = 0
    carve(1,1)
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(['#' if cell else ' ' for cell in row]))

def solve_maze(maze):
    n, m = len(maze), len(maze[0])
    stack = [(1,1)]
    visited = set()
    while stack:
        x, y = stack.pop()
        if (x, y) == (n-2, m-2):
            return True
        visited.add((x, y))
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0 and (nx, ny) not in visited:
                stack.append((nx, ny))
    return False

if __name__ == "__main__":
    n, m = 15, 15
    maze = generate_maze(n, m)
    print_maze(maze)
    print("Solvable?", solve_maze(maze))
