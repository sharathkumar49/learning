"""
LeetCode 2785. Sort Vowels in a String

Given s, return the string after sorting vowels.

Constraints:
- 1 <= s.length <= 10^5
"""

def sortVowels(s):
    vowels = [c for c in s if c in 'aeiouAEIOU']
    vowels.sort()
    res = []
    j = 0
    for c in s:
        if c in 'aeiouAEIOU':
            res.append(vowels[j])
            j += 1
        else:
            res.append(c)
    return ''.join(res)
# Example usage:
# print(sortVowels("lEetcOde"))  # Output: "lEOtcede"
