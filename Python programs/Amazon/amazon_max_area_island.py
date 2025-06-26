# Amazon: Maximum Area of Island (DFS in grid)
def max_area_of_island(grid):
    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
    max_area = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))
    return max_area

if __name__ == "__main__":
    m = int(input("Rows: "))
    n = int(input("Cols: "))
    grid = [list(map(int, input().split())) for _ in range(m)]
    print("Max area:", max_area_of_island(grid))
