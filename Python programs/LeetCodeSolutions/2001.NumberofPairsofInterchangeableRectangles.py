"""
LeetCode 2001. Number of Pairs of Interchangeable Rectangles

Given n rectangles, where the i-th rectangle has width[i] and height[i], return the number of pairs of rectangles that are interchangeable. Two rectangles are interchangeable if they have the same width-to-height ratio.

Example:
Input: rectangles = [[4,8],[3,6],[10,20],[15,30]]
Output: 6

Constraints:
- 1 <= rectangles.length <= 10^5
- rectangles[i].length == 2
- 1 <= width[i], height[i] <= 10^5
"""

def interchangeableRectangles(rectangles):
    from collections import Counter
    from fractions import Fraction
    ratios = [Fraction(w, h) for w, h in rectangles]
    count = Counter(ratios)
    return sum(v * (v - 1) // 2 for v in count.values())

# Example usage:
# print(interchangeableRectangles([[4,8],[3,6],[10,20],[15,30]]))  # Output: 6
