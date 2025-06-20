"""
835. Image Overlap

You are given two binary matrices img1 and img2. Return the largest possible overlap by sliding img1 over img2.

Example 1:
Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3

Constraints:
- n == img1.length == img1[i].length == img2.length == img2[i].length
- 1 <= n <= 30
- img1[i][j], img2[i][j] is 0 or 1.
"""
def largestOverlap(img1, img2):
    n = len(img1)
    A = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
    B = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]
    count = {}
    for (i1, j1) in A:
        for (i2, j2) in B:
            delta = (i1 - i2, j1 - j2)
            count[delta] = count.get(delta, 0) + 1
    return max(count.values() or [0])

# Example usage:
print(largestOverlap([[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]]))  # Output: 3
