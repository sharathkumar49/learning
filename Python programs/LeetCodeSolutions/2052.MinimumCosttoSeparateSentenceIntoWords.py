"""
LeetCode 2052. Minimum Cost to Separate Sentence Into Words

Given a string sentence and a list of valid words, return the minimum cost to separate the sentence into valid words. If not possible, return -1.

Example:
Input: sentence = "leetcode", validWords = ["leet","code"]
Output: 0

Constraints:
- 1 <= sentence.length <= 1000
- 1 <= validWords.length <= 100
"""

def minCostToSeparate(sentence, validWords):
    n = len(sentence)
    word_set = set(validWords)
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        for w in validWords:
            if i >= len(w) and sentence[i-len(w):i] == w:
                dp[i] = min(dp[i], dp[i-len(w)])
        dp[i] = min(dp[i], dp[i-1] + 1)
    return dp[n] if dp[n] != float('inf') else -1

# Example usage:
# print(minCostToSeparate("leetcode", ["leet","code"]))  # Output: 0
