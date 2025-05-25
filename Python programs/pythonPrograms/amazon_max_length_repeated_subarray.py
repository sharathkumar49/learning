# Amazon: Find the Maximum Length of Repeated Subarray
# Given two integer arrays A and B, return the length of the longest common subarray.

def find_length(A, B):
    m, n = len(A), len(B)
    dp = [[0]*(n+1) for _ in range(m+1)]
    res = 0
    for i in range(m):
        for j in range(n):
            if A[i] == B[j]:
                dp[i+1][j+1] = dp[i][j] + 1
                res = max(res, dp[i+1][j+1])
    return res

if __name__ == "__main__":
    print(find_length([1,2,3,2,1], [3,2,1,4,7]))  # Output: 3
