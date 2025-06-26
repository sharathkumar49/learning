# Facebook: Find the Longest Palindromic Subsequence
# Given a string s, find the length of the longest palindromic subsequence in s.

def longest_palindromic_subseq(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

if __name__ == "__main__":
    s1 = "bbbab"
    print(longest_palindromic_subseq(s1))  # Output: 4
    s2 = "cbbd"
    print(longest_palindromic_subseq(s2))  # Output: 2
