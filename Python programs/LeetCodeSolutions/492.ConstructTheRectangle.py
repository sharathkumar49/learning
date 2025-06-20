"""
492. Construct the Rectangle

Given an integer area, return the dimensions of the rectangle (length and width) such that the area is equal to length * width, the length is as large as possible, and the length >= width.

Constraints:
- 1 <= area <= 10^7

Example:
Input: area = 4
Output: [2,2]
"""

import math

class Solution:
    def constructRectangle(self, area: int) -> list:
        w = int(math.sqrt(area))
        while area % w != 0:
            w -= 1
        return [area // w, w]

# Example usage:
sol = Solution()
print(sol.constructRectangle(4))  # Output: [2, 2]
