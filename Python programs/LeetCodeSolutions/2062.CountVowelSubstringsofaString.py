"""
LeetCode 2062. Count Vowel Substrings of a String

Given a string word, return the number of substrings that contain only vowels and all five vowels at least once.

Example:
Input: word = "aeiouu"
Output: 2

Constraints:
- 1 <= word.length <= 100
- word consists only of lowercase English letters.
"""

def countVowelSubstrings(word):
    vowels = set('aeiou')
    n = len(word)
    res = 0
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if word[j] not in vowels:
                break
            seen.add(word[j])
            if len(seen) == 5:
                res += 1
    return res

# Example usage:
# print(countVowelSubstrings("aeiouu"))  # Output: 2
