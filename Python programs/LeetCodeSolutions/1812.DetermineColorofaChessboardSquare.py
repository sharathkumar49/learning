"""
LeetCode 1812. Determine Color of a Chessboard Square

Given a string coordinates, return true if the square is white, false if black.

Example 1:
Input: coordinates = "a1"
Output: false

Constraints:
- coordinates.length == 2
- 'a' <= coordinates[0] <= 'h'
- '1' <= coordinates[1] <= '8'
"""

def squareIsWhite(coordinates):
    return (ord(coordinates[0]) - ord('a') + int(coordinates[1])) % 2 == 1

# Example usage:
# coordinates = "a1"
# print(squareIsWhite(coordinates))  # Output: False
