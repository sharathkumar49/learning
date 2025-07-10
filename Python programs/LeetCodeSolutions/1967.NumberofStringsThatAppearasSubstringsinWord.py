"""
LeetCode 1967. Number of Strings That Appear as Substrings in Word

Given an array patterns and a string word, return the number of patterns that appear as substrings in word.

Example:
Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3

Constraints:
- 1 <= patterns.length <= 100
- 1 <= patterns[i].length <= 100
- 1 <= word.length <= 100
"""

def numOfStrings(patterns, word):
    return sum(p in word for p in patterns)

# Example usage:
# print(numOfStrings(["a","abc","bc","d"], "abc"))  # Output: 3
