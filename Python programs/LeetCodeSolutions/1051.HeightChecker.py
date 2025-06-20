"""
1051. Height Checker

Given an array heights representing the heights of students, return the number of students not standing in the right positions (i.e., not in non-decreasing order).

Constraints:
- 1 <= heights.length <= 100
- 1 <= heights[i] <= 100

Example:
Input: heights = [1,1,4,2,1,3]
Output: 3
"""
from typing import List

def heightChecker(heights: List[int]) -> int:
    return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))

# Example usage:
heights = [1,1,4,2,1,3]
print(heightChecker(heights))  # Output: 3
