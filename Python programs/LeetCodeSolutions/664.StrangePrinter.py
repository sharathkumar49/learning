"""
664. Strange Printer
Difficulty: Hard

There is a strange printer with the following two special requirements:
- Each turn, the printer can print a sequence of the same character.
- Each new turn, the printer can only print new characters on top of the previous print.
Given a string s, return the minimum number of turns the printer needed to print it.

Example 1:
Input: s = "aaabbb"
Output: 2

Example 2:
Input: s = "aba"
Output: 2

Constraints:
1 <= s.length <= 100
s consists of lowercase English letters.
"""

def strangePrinter(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            dp[i][j] = dp[i+1][j] + 1
            for k in range(i+1, j+1):
                if s[k] == s[i]:
                    dp[i][j] = min(dp[i][j], dp[i][k-1] + dp[k][j])
    return dp[0][n-1]

# Example usage
if __name__ == "__main__":
    print(strangePrinter("aaabbb"))  # Output: 2
    print(strangePrinter("aba"))     # Output: 2
