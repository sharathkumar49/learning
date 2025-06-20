"""
1072. Flip Columns For Maximum Number of Equal Rows

Given a matrix, return the maximum number of rows that have all values equal after flipping any number of columns.

Constraints:
- 1 <= matrix.length <= 300
- 1 <= matrix[0].length <= 300

Example:
Input: matrix = [[0,1],[1,1]]
Output: 1
"""
from typing import List

def maxEqualRowsAfterFlips(matrix: List[List[int]]) -> int:
    from collections import Counter
    patterns = [tuple(row[i] ^ row[0] for i in range(len(row))) for row in matrix]
    return Counter(patterns).most_common(1)[0][1]

# Example usage:
matrix = [[0,1],[1,1]]
print(maxEqualRowsAfterFlips(matrix))  # Output: 1
