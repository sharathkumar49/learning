"""
861. Score After Flipping Matrix

Given a binary matrix A, we can flip any row or column. After any number of flips, each row is interpreted as a binary number and the score is the sum of these numbers. Return the highest possible score.

Example 1:
Input: A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39

Constraints:
- 1 <= A.length, A[0].length <= 20
- A[i][j] is 0 or 1.
"""
def matrixScore(A):
    m, n = len(A), len(A[0])
    for i in range(m):
        if A[i][0] == 0:
            for j in range(n):
                A[i][j] ^= 1
    for j in range(1, n):
        if sum(A[i][j] for i in range(m)) < m / 2:
            for i in range(m):
                A[i][j] ^= 1
    return sum(int(''.join(map(str, row)), 2) for row in A)

# Example usage:
print(matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))  # Output: 39
