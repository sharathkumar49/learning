"""
LeetCode 1974. Minimum Time to Type Word Using Special Typewriter

Given a string word, return the minimum time to type it using a special typewriter.

Example:
Input: word = "abc"
Output: 5

Constraints:
- 1 <= word.length <= 100
- word consists of lowercase English letters.
"""

def minTimeToType(word):
    res = len(word)
    prev = 'a'
    for c in word:
        diff = abs(ord(c) - ord(prev))
        res += min(diff, 26 - diff)
        prev = c
    return res

# Example usage:
# print(minTimeToType("abc"))  # Output: 5
