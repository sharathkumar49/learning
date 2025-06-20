"""
1105. Filling Bookcase Shelves

You are given a list of books, where books[i] = [thickness, height], and an integer shelf_width. Arrange the books on shelves to minimize the total height of the bookcase.

Constraints:
- 1 <= books.length <= 1000
- 1 <= thicknessi <= shelf_width <= 1000
- 1 <= heighti <= 1000

Example:
Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
Output: 6
"""
from typing import List

def minHeightShelves(books: List[List[int]], shelf_width: int) -> int:
    n = len(books)
    dp = [0] + [float('inf')] * n
    for i in range(1, n+1):
        width = 0
        height = 0
        for j in range(i, 0, -1):
            width += books[j-1][0]
            if width > shelf_width:
                break
            height = max(height, books[j-1][1])
            dp[i] = min(dp[i], dp[j-1] + height)
    return dp[n]

# Example usage:
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelf_width = 4
print(minHeightShelves(books, shelf_width))  # Output: 6
