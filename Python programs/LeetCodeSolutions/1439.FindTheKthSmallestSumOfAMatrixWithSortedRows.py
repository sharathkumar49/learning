"""
LeetCode 1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows

Given a m x n matrix mat where each row is sorted in non-decreasing order, and an integer k, return the kth smallest sum of a matrix with sorted rows.

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 40
- 1 <= k <= min(200, n^m)
- 1 <= mat[i][j] <= 5000

Example:
Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 17
"""
import heapq

def kthSmallest(mat, k):
    m, n = len(mat), len(mat[0])
    res = mat[0]
    for i in range(1, m):
        res = merge(res, mat[i], k)
    return res[k-1]

def merge(a, b, k):
    heap = []
    for i in range(len(a)):
        for j in range(len(b)):
            heapq.heappush(heap, a[i]+b[j])
    res = []
    for _ in range(k):
        res.append(heapq.heappop(heap))
    return res

# Example usage:
mat = [[1,3,11],[2,4,6]]
k = 5
print(kthSmallest(mat, k))  # Output: 17
