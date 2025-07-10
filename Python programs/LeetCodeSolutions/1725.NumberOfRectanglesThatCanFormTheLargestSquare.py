"""
LeetCode 1725. Number Of Rectangles That Can Form The Largest Square

Given a list of rectangles, return the number of rectangles that can form the largest square.

Example 1:
Input: rectangles = [[5,8],[3,9],[5,12],[16,5]]
Output: 3

Constraints:
- 1 <= rectangles.length <= 1000
- rectangles[i].length == 2
- 1 <= rectangles[i][j] <= 10^9
"""

def countGoodRectangles(rectangles):
    maxLen = 0
    count = 0
    for a, b in rectangles:
        side = min(a, b)
        if side > maxLen:
            maxLen = side
            count = 1
        elif side == maxLen:
            count += 1
    return count

# Example usage:
# rectangles = [[5,8],[3,9],[5,12],[16,5]]
# print(countGoodRectangles(rectangles))  # Output: 3
