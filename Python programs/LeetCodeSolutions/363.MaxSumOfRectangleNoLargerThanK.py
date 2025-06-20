"""
363. Max Sum of Rectangle No Larger Than K

Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -100 <= matrix[i][j] <= 100
- -10^5 <= k <= 10^5
"""
from typing import List
import bisect

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = float('-inf')
        for left in range(n):
            row_sum = [0] * m
            for right in range(left, n):
                for i in range(m):
                    row_sum[i] += matrix[i][right]
                prefix = [0]
                curr_sum = 0
                for sum_ in row_sum:
                    curr_sum += sum_
                    idx = bisect.bisect_left(prefix, curr_sum - k)
                    if idx < len(prefix):
                        res = max(res, curr_sum - prefix[idx])
                    bisect.insort(prefix, curr_sum)
        return res

# Example usage:
matrix = [
  [1,0,1],
  [0,-2,3]
]
k = 2
print(Solution().maxSumSubmatrix(matrix, k))  # Output: 2
