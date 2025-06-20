"""
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.

Constraints:
- 1 <= numRows <= 30

Example:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""
from typing import List

def generate(numRows: int) -> List[List[int]]:
    res = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = res[i-1][j-1] + res[i-1][j]
        res.append(row)
    return res

# Example usage:
if __name__ == "__main__":
    print(generate(5))  # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
