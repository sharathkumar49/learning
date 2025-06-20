"""
LeetCode 748. Shortest Completing Word

Given a string licensePlate and an array of strings words, return the shortest completing word in words.
A completing word is a word that contains all the letters in licensePlate (ignoring digits, spaces, and case).

Example 1:
Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"

Example 2:
Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
Output: "pest"

Constraints:
- 1 <= licensePlate.length <= 7
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 15
- licensePlate contains at least one letter.
"""
from typing import List
from collections import Counter

def shortestCompletingWord(licensePlate: str, words: List[str]) -> str:
    cnt = Counter(c.lower() for c in licensePlate if c.isalpha())
    res = None
    for word in words:
        wcnt = Counter(word)
        if all(wcnt[c] >= cnt[c] for c in cnt):
            if res is None or len(word) < len(res):
                res = word
    return res

# Example usage
if __name__ == "__main__":
    print(shortestCompletingWord("1s3 PSt", ["step","steps","stripe","stepple"]))  # Output: "steps"
    print(shortestCompletingWord("1s3 456", ["looks","pest","stew","show"]))      # Output: "pest"
