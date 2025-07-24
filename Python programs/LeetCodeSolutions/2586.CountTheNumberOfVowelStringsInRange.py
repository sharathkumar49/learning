"""
LeetCode 2586. Count the Number of Vowel Strings in Range

Given words and a range, return the number of vowel strings in the range.

Constraints:
- 1 <= words.length <= 100
"""

def vowelStrings(words, left, right):
    vowels = set('aeiou')
    return sum(words[i][0] in vowels and words[i][-1] in vowels for i in range(left, right+1))
# Example usage:
# print(vowelStrings(["aba","bcb","ece","aa","e"], 0, 2))  # Output: 2
