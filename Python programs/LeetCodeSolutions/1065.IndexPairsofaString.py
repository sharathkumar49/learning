"""
1065. Index Pairs of a String

Given a text string and an array of words, return all index pairs [i, j] such that the substring text[i..j] is in words.

Constraints:
- 1 <= text.length <= 100
- 1 <= words.length <= 20
- 1 <= words[i].length <= 50

Example:
Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
Output: [[3,7],[9,13]]
"""
from typing import List

def indexPairs(text: str, words: List[str]) -> List[List[int]]:
    res = []
    for word in words:
        start = text.find(word)
        while start != -1:
            res.append([start, start + len(word) - 1])
            start = text.find(word, start + 1)
    return sorted(res)

# Example usage:
text = "thestoryofleetcodeandme"
words = ["story","fleet","leetcode"]
print(indexPairs(text, words))  # Output: [[3, 7], [9, 13]]
