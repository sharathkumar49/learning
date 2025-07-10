"""
LeetCode 2063. Vowels of All Substrings

Given a string word, return the sum of the number of vowels in every substring of word.

Example:
Input: word = "aba"
Output: 6

Constraints:
- 1 <= word.length <= 10^5
- word consists only of lowercase English letters.
"""

def countVowels(word):
    n = len(word)
    res = 0
    for i, c in enumerate(word):
        if c in 'aeiou':
            res += (i+1)*(n-i)
    return res

# Example usage:
# print(countVowels("aba"))  # Output: 6
