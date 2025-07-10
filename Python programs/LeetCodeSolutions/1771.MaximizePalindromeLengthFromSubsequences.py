"""
LeetCode 1771. Maximize Palindrome Length From Subsequences

Given two strings word1 and word2, return the maximum length of a palindrome that can be built by concatenating a non-empty subsequence of word1 and a non-empty subsequence of word2.

Example 1:
Input: word1 = "cacb", word2 = "cbba"
Output: 5

Constraints:
- 1 <= word1.length, word2.length <= 1000
- word1 and word2 consist of lowercase English letters
"""

def longestPalindrome(word1, word2):
    s = word1 + word2
    n, m = len(word1), len(word2)
    dp = [[0]*len(s) for _ in range(len(s))]
    for i in range(len(s)-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    res = 0
    for i in range(n):
        for j in range(n, n+m):
            if word1[i] == word2[j-n]:
                res = max(res, dp[i][j])
    return res

# Example usage:
# word1 = "cacb"
# word2 = "cbba"
# print(longestPalindrome(word1, word2))  # Output: 5
