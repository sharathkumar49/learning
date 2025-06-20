"""
533. Lonely Pixel II

Given a picture consisting of black and white pixels, return the number of black lonely pixels in the picture.
A black lonely pixel is a character 'B' that is located at a specific position where both the row and column it is in contains exactly N black pixels and all rows that have a black pixel at column j are exactly the same.

Constraints:
- m == picture.length
- n == picture[i].length
- 1 <= m, n <= 200
- picture[i][j] is 'B' or 'W'.
- 1 <= N <= min(m, n)

Example:
Input: picture = [["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","W","B","W","B","W"]], N = 3
Output: 6
"""

from collections import Counter

class Solution:
    def findBlackPixel(self, picture: list, N: int) -> int:
        m, n = len(picture), len(picture[0])
        row_count = [row.count('B') for row in picture]
        col_count = [sum(picture[i][j] == 'B' for i in range(m)) for j in range(n)]
        row_strs = [''.join(row) for row in picture]
        row_counter = Counter(row_strs)
        res = 0
        for i in range(m):
            if row_count[i] != N:
                continue
            for j in range(n):
                if picture[i][j] == 'B' and col_count[j] == N:
                    if all(row_strs[x] == row_strs[i] for x in range(m) if picture[x][j] == 'B') and row_counter[row_strs[i]] >= N:
                        res += 1
        return res

# Example usage:
picture = [["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","W","B","W","B","W"]]
sol = Solution()
print(sol.findBlackPixel(picture, 3))  # Output: 6
