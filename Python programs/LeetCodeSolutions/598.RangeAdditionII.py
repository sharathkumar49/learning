"""
598. Range Addition II
Difficulty: Easy

You are given an m x n matrix M initialized with all 0's and a list of operations ops, where ops[i] = [ai, bi]. Each operation increments by 1 all the cells in the rectangle defined by (0, 0) to (ai - 1, bi - 1).
Return the number of maximum integers in the matrix after performing all the operations.

Example 1:
Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4

Constraints:
1 <= m, n <= 4 * 10^4
0 <= ops.length <= 10^4
ops[i].length == 2
1 <= ai <= m
1 <= bi <= n
"""

def maxCount(m, n, ops):
    if not ops:
        return m * n
    min_a = min(op[0] for op in ops)
    min_b = min(op[1] for op in ops)
    return min_a * min_b

# Example usage
if __name__ == "__main__":
    print(maxCount(3, 3, [[2,2],[3,3]]))  # Output: 4
