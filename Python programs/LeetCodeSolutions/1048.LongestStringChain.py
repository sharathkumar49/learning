"""
1048. Longest String Chain

Given a list of words, each word can be a predecessor of another if you can add a single letter anywhere in the predecessor to make it the other word. Return the length of the longest possible word chain.

Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 16
- words[i] consists only of lowercase English letters.

Example:
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: The longest chain is "a" -> "ba" -> "bda" -> "bdca".
"""
from typing import List

def longestStrChain(words: List[str]) -> int:
    words.sort(key=len)
    dp = {}
    res = 1
    for word in words:
        dp[word] = 1
        for i in range(len(word)):
            prev = word[:i] + word[i+1:]
            if prev in dp:
                dp[word] = max(dp[word], dp[prev] + 1)
        res = max(res, dp[word])
    return res

# Example usage:
words = ["a","b","ba","bca","bda","bdca"]
print(longestStrChain(words))  # Output: 4
