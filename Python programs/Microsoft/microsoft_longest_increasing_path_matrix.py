# Microsoft: Find the Longest Increasing Path in a Matrix
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

def longest_increasing_path(matrix):
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    memo = [[0]*n for _ in range(m)]
    def dfs(i, j):
        if memo[i][j]:
            return memo[i][j]
        val = matrix[i][j]
        for x, y in [(0,1),(1,0),(0,-1),(-1,0)]:
            ni, nj = i + x, j + y
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > val:
                memo[i][j] = max(memo[i][j], dfs(ni, nj))
        memo[i][j] += 1
        return memo[i][j]
    return max(dfs(i, j) for i in range(m) for j in range(n))

if __name__ == "__main__":
    mat1 = [
        [9,9,4],
        [6,6,8],
        [2,1,1]
    ]
    print(longest_increasing_path(mat1))  # Output: 4
    mat2 = [
        [3,4,5],
        [3,2,6],
        [2,2,1]
    ]
    print(longest_increasing_path(mat2))  # Output: 4
