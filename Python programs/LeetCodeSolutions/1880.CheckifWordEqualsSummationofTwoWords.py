"""
LeetCode 1880. Check if Word Equals Summation of Two Words

Given three strings firstWord, secondWord, and targetWord, each representing a non-negative integer where each letter represents a digit (a=0, b=1, ..., j=9), return true if the sum of the first two is equal to the third.

Example:
Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
Output: true

Constraints:
- 1 <= firstWord.length, secondWord.length, targetWord.length <= 8
- firstWord, secondWord, targetWord consist of lowercase English letters from 'a' to 'j'.
"""

def isSumEqual(firstWord, secondWord, targetWord):
    def wordToNum(word):
        return int(''.join(str(ord(c) - ord('a')) for c in word))
    return wordToNum(firstWord) + wordToNum(secondWord) == wordToNum(targetWord)

# Example usage:
# print(isSumEqual("acb", "cba", "cdb"))  # Output: True
