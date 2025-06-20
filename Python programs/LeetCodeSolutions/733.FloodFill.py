"""
LeetCode 733. Flood Fill

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and newColor. Flood fill the image starting from the pixel image[sr][sc].

Return the modified image after performing the flood fill.

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

Constraints:
- m == image.length
- n == image[i].length
- 1 <= m, n <= 50
- 0 <= image[i][j], newColor < 2^16
- 0 <= sr < m
- 0 <= sc < n
"""
from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    m, n = len(image), len(image[0])
    color = image[sr][sc]
    if color == newColor:
        return image
    def dfs(x, y):
        if 0 <= x < m and 0 <= y < n and image[x][y] == color:
            image[x][y] = newColor
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                dfs(x+dx, y+dy)
    dfs(sr, sc)
    return image

# Example usage
if __name__ == "__main__":
    print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))  # Output: [[2,2,2],[2,2,0],[2,0,1]]
