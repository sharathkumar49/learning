"""
583. Delete Operation for Two Strings
Difficulty: Medium

Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4

Constraints:
1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
"""

def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if word1[i] == word2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return m + n - 2*dp[m][n]

# Example usage
if __name__ == "__main__":
    print(minDistance("sea", "eat"))        # Output: 2
    print(minDistance("leetcode", "etco"))  # Output: 4
