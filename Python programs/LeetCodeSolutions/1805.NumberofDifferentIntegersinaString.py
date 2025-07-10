"""
LeetCode 1805. Number of Different Integers in a String

Given a string word, return the number of different integers in the string.

Example 1:
Input: word = "a123bc34d8ef34"
Output: 3

Constraints:
- 1 <= word.length <= 1000
- word consists of digits and lowercase English letters
"""

def numDifferentIntegers(word):
    import re
    return len(set(map(lambda x: x.lstrip('0') or '0', re.findall(r'\d+', word))))

# Example usage:
# word = "a123bc34d8ef34"
# print(numDifferentIntegers(word))  # Output: 3
