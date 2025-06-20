"""
813. Largest Sum of Averages

Given an array A, partition it into at most K adjacent (non-empty) groups, then the score is the sum of the averages of each group. Return the largest score possible.

Example 1:
Input: A = [9,1,2,3,9], K = 3
Output: 20.0

Constraints:
- 1 <= A.length <= 100
- 1 <= K <= A.length
- 0 <= A[i] <= 10^4
"""
def largestSumOfAverages(A, K):
    n = len(A)
    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + A[i]
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = (prefix[n] - prefix[i-1]) / (n - i + 1)
    for k in range(1, K):
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                dp[i] = max(dp[i], (prefix[j-1] - prefix[i-1]) / (j - i) + dp[j])
    return dp[1]

# Example usage:
print(largestSumOfAverages([9,1,2,3,9], 3))  # Output: 20.0
