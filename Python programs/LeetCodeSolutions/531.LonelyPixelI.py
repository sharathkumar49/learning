"""
531. Lonely Pixel I

Given a picture consisting of black and white pixels, return the number of black lonely pixels.
A black lonely pixel is a character 'B' that is located at a specific position where both the row and column it is in contains no other black pixels.

Constraints:
- m == picture.length
- n == picture[i].length
- 1 <= m, n <= 500
- picture[i][j] is 'B' or 'W'.

Example:
Input: picture = [["W","B","W"],["W","W","B"],["B","W","W"]]
Output: 3
"""

class Solution:
    def findLonelyPixel(self, picture: list) -> int:
        m, n = len(picture), len(picture[0])
        row = [0] * m
        col = [0] * n
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row[i] += 1
                    col[j] += 1
        res = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B' and row[i] == 1 and col[j] == 1:
                    res += 1
        return res

# Example usage:
picture = [["W","B","W"],["W","W","B"],["B","W","W"]]
sol = Solution()
print(sol.findLonelyPixel(picture))  # Output: 3
