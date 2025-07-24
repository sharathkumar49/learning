"""
LeetCode 2942. Find Words Containing Character

Given words and x, return the indices of words containing x.

Constraints:
- 1 <= words.length <= 100
- x is a lowercase English letter
"""

def findWordsContaining(words, x):
    return [i for i, word in enumerate(words) if x in word]
# Example usage:
# print(findWordsContaining(["leet","code"], "e"))  # Output: [0,1]
