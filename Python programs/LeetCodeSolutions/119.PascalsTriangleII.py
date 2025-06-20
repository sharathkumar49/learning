"""
119. Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/

Given an integer rowIndex, return the rowIndex-th (0-indexed) row of the Pascal's triangle.

Constraints:
- 0 <= rowIndex <= 33

Example:
Input: rowIndex = 3
Output: [1,3,3,1]
"""
from typing import List

def getRow(rowIndex: int) -> List[int]:
    row = [1]
    for _ in range(rowIndex):
        row = [x + y for x, y in zip([0]+row, row+[0])]
    return row

# Example usage:
if __name__ == "__main__":
    print(getRow(3))  # Output: [1,3,3,1]
    print(getRow(0))  # Output: [1]
