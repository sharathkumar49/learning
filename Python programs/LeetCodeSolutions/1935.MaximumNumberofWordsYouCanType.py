"""
LeetCode 1935. Maximum Number of Words You Can Type

Given a string text and a string brokenLetters, return the number of words you can fully type.

Example:
Input: text = "hello world", brokenLetters = "ad"
Output: 1

Constraints:
- 1 <= text.length <= 10^4
- 0 <= brokenLetters.length <= 26
- text and brokenLetters consist of lowercase English letters and spaces.
"""

def canBeTypedWords(text, brokenLetters):
    broken = set(brokenLetters)
    return sum(not set(word) & broken for word in text.split())

# Example usage:
# print(canBeTypedWords("hello world", "ad"))  # Output: 1
