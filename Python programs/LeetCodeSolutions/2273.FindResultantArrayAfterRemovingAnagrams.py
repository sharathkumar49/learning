"""
LeetCode 2273. Find Resultant Array After Removing Anagrams

Given words, return the resultant array after removing anagrams.

Example:
Input: words = ["abba","baba","bbaa","cd","cd"]
Output: ["abba","cd"]

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 10
"""

def removeAnagrams(words):
    res = []
    prev = ''
    for w in words:
        if sorted(w) != sorted(prev):
            res.append(w)
        prev = w
    return res

# Example usage:
# print(removeAnagrams(["abba","baba","bbaa","cd","cd"]))  # Output: ["abba","cd"]
