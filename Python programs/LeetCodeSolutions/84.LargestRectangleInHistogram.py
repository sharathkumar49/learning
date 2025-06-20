"""
84. Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Constraints:
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4

Example:
Input: heights = [2,1,5,6,2,3]
Output: 10
"""
from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    stack = []
    max_area = 0
    heights.append(0)
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area

# Example usage:
if __name__ == "__main__":
    print(largestRectangleArea([2,1,5,6,2,3]))  # Output: 10
    print(largestRectangleArea([2,4]))         # Output: 4
