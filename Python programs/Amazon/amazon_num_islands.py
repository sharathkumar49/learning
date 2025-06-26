# Amazon: Find the number of islands in a grid (DFS)
def num_islands(grid):
    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count

if __name__ == "__main__":
    m = int(input("Rows: "))
    n = int(input("Cols: "))
    grid = [list(input().strip()) for _ in range(m)]
    print("Number of islands:", num_islands(grid))
