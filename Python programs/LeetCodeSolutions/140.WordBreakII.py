"""
140. Word Break II
https://leetcode.com/problems/word-break-ii/

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Constraints:
- 1 <= s.length <= 20
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters.

Example:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
"""
from typing import List

def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    word_set = set(wordDict)
    memo = {}
    def dfs(start):
        if start == len(s):
            return ['']
        if start in memo:
            return memo[start]
        res = []
        for end in range(start+1, len(s)+1):
            word = s[start:end]
            if word in word_set:
                for sub in dfs(end):
                    res.append(word + ('' if not sub else ' ' + sub))
        memo[start] = res
        return res
    return dfs(0)

# Example usage:
if __name__ == "__main__":
    print(wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))  # Output: ["cats and dog","cat sand dog"]
    print(wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))
