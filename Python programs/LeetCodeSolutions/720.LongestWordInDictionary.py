"""
LeetCode 720. Longest Word in Dictionary

Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.
If there is more than one possible answer, return the longest word with the smallest lexicographical order.

Example 1:
Input: words = ["w","wo","wor","worl","world"]
Output: "world"

Example 2:
Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"

Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 30
- words[i] consists of lowercase English letters.
"""
from typing import List

def longestWord(words: List[str]) -> str:
    words.sort()
    built = set([''])
    res = ''
    for word in words:
        if word[:-1] in built:
            built.add(word)
            if len(word) > len(res):
                res = word
    return res

# Example usage
if __name__ == "__main__":
    print(longestWord(["w","wo","wor","worl","world"]))  # Output: "world"
    print(longestWord(["a","banana","app","appl","ap","apply","apple"]))  # Output: "apple"
