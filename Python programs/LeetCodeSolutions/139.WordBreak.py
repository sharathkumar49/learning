"""
139. Word Break
https://leetcode.com/problems/word-break/

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Constraints:
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters.

Example:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
"""
from typing import List

def wordBreak(s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[-1]

# Example usage:
if __name__ == "__main__":
    print(wordBreak("leetcode", ["leet","code"]))  # Output: True
    print(wordBreak("applepenapple", ["apple","pen"]))  # Output: True
    print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))  # Output: False
