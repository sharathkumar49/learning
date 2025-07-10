"""
LeetCode 1858. Longest Word With All Prefixes

Given an array of strings words, return the longest word in words such that every prefix of the word is also in words. If there are multiple answers, return the lexicographically smallest one.

Example 1:
Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"

Constraints:
- 1 <= words.length <= 10^5
- 1 <= words[i].length <= 10^5
- All words[i] are lowercase English letters.
"""

def longestWord(words):
    words = set(words)
    ans = ""
    for w in sorted(words):
        if all(w[:i] in words for i in range(1, len(w))):
            if len(w) > len(ans) or (len(w) == len(ans) and w < ans):
                ans = w
    return ans

# Example usage:
# words = ["a","banana","app","appl","ap","apply","apple"]
# print(longestWord(words))  # Output: "apple"
