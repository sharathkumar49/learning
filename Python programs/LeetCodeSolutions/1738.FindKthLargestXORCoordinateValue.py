"""
LeetCode 1738. Find Kth Largest XOR Coordinate Value

Given a matrix, return the kth largest value of the XOR of all elements from (0,0) to (i,j).

Example 1:
Input: matrix = [[5,2],[1,6]], k = 1
Output: 7

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 1000
- 0 <= matrix[i][j] <= 10^6
- 1 <= k <= m * n
"""

def kthLargestValue(matrix, k):
    m, n = len(matrix), len(matrix[0])
    pre = [[0]*(n+1) for _ in range(m+1)]
    vals = []
    for i in range(1, m+1):
        for j in range(1, n+1):
            pre[i][j] = pre[i-1][j] ^ pre[i][j-1] ^ pre[i-1][j-1] ^ matrix[i-1][j-1]
            vals.append(pre[i][j])
    vals.sort(reverse=True)
    return vals[k-1]

# Example usage:
# matrix = [[5,2],[1,6]]
# k = 1
# print(kthLargestValue(matrix, k))  # Output: 7
