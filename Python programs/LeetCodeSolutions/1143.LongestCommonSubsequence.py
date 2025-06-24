"""
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.

Example:
Input: text1 = "abcde", text2 = "ace"
Output: 3

"""
def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    return dp[0][0]

# Example usage
if __name__ == "__main__":
    print(longestCommonSubsequence("abcde", "ace"))  # Output: 3
