"""
LeetCode 2370. Longest Ideal Subsequence

Given s and k, return the length of the longest ideal subsequence.

Example:
Input: s = "acfgbd", k = 2
Output: 4

Constraints:
- 1 <= s.length <= 10^5
- 0 <= k <= 25
"""

def longestIdealString(s, k):
    dp = [0]*128
    for c in s:
        idx = ord(c)
        dp[idx] = max(dp[max(0,idx-k):idx+k+1]) + 1
    return max(dp)

# Example usage:
# print(longestIdealString("acfgbd", 2))  # Output: 4
