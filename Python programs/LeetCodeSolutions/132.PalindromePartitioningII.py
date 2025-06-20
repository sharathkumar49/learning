"""
132. Palindrome Partitioning II
https://leetcode.com/problems/palindrome-partitioning-ii/

Given a string s, partition s such that every substring of the partition is a palindrome. Return the minimum cuts needed for a palindrome partitioning of s.

Constraints:
- 1 <= s.length <= 2000
- s consists of only lowercase English letters.

Example:
Input: s = "aab"
Output: 1
"""
def minCut(s: str) -> int:
    n = len(s)
    dp = [0] * n
    is_palindrome = [[False]*n for _ in range(n)]
    for i in range(n):
        min_cut = i
        for j in range(i+1):
            if s[j] == s[i] and (i-j <= 1 or is_palindrome[j+1][i-1]):
                is_palindrome[j][i] = True
                min_cut = 0 if j == 0 else min(min_cut, dp[j-1]+1)
        dp[i] = min_cut
    return dp[-1]

# Example usage:
if __name__ == "__main__":
    print(minCut("aab"))  # Output: 1
    print(minCut("a"))    # Output: 0
