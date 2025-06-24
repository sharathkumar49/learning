"""
LeetCode 1278. Palindrome Partitioning III

Given a string s and an integer k, partition s into k substrings such that the sum of the minimum number of characters that need to be changed to make each substring a palindrome is minimized. Return the minimum possible sum.

Constraints:
- 1 <= k <= s.length <= 100
- s consists of lowercase English letters only.

Example:
Input: s = "abc", k = 2
Output: 1
"""
def palindromePartition(s, k):
    n = len(s)
    cost = [[0]*n for _ in range(n)]
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            cost[i][j] = cost[i+1][j-1] + (s[i] != s[j])
    dp = [[float('inf')]*(k+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(1, n+1):
        for kk in range(1, min(k, i)+1):
            for j in range(kk-1, i):
                dp[i][kk] = min(dp[i][kk], dp[j][kk-1] + cost[j][i-1])
    return dp[n][k]

# Example usage:
s = "abc"
k = 2
print(palindromePartition(s, k))  # Output: 1
