"""
LeetCode 1639. Number of Ways to Form a Target String Given a Dictionary

Given a list of words and a target string, return the number of ways to form the target string by choosing a character from a column of the words at each step.

Example 1:
Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6

Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length, target.length <= 1000
- words[i] and target consist of lowercase English letters.
"""

def numWays(words, target):
    mod = 10**9+7
    m, n = len(target), len(words[0])
    from collections import Counter
    count = [Counter(w[i] for w in words) for i in range(n)]
    dp = [1] + [0]*m
    for i in range(n):
        for j in range(m-1, -1, -1):
            dp[j+1] += dp[j] * count[i][target[j]]
            dp[j+1] %= mod
    return dp[m]

# Example usage:
# words = ["acca","bbbb","caca"]
# target = "aba"
# print(numWays(words, target))  # Output: 6
