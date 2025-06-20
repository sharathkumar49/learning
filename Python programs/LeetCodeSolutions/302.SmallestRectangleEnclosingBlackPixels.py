"""
302. Smallest Rectangle Enclosing Black Pixels

You are given an m x n binary matrix image where 0 represents a white pixel and 1 represents a black pixel.
The black pixels are connected (i.e., there is only one black region). Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

Constraints:
- m == image.length
- n == image[i].length
- 1 <= m, n <= 100
- image[i][j] is either '0' or '1'.
- 1 <= x < m
- 1 <= y < n
- The black pixels are connected.
"""
from typing import List

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])
        left = right = y
        top = bottom = x
        for i in range(m):
            for j in range(n):
                if image[i][j] == '1':
                    left = min(left, j)
                    right = max(right, j)
                    top = min(top, i)
                    bottom = max(bottom, i)
        return (bottom - top + 1) * (right - left + 1)

# Example usage:
image = [
    ["0","0","1","0"],
    ["0","1","1","0"],
    ["0","1","0","0"]
]
x, y = 0, 2
print(Solution().minArea(image, x, y))  # Output: 6
