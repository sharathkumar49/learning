"""
1216. Valid Palindrome III

Given a string s and an integer k, return True if s can be transformed into a palindrome by removing at most k characters.

Constraints:
- 1 <= s.length <= 1000
- s consists of only lowercase English letters.
- 0 <= k <= s.length

Example:
Input: s = "abcdeca", k = 2
Output: True

"""
def isValidPalindrome(s, k):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1] <= k

# Example usage
if __name__ == "__main__":
    print(isValidPalindrome("abcdeca", 2))  # Output: True
