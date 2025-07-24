"""
LeetCode 2828. Check if a String Is an Acronym of Words

Given words and s, return True if s is an acronym of words.

Constraints:
- 1 <= words.length <= 100
- 1 <= s.length <= 100
"""

def isAcronym(words, s):
    return ''.join(word[0] for word in words) == s
# Example usage:
# print(isAcronym(["alice","bob","charlie"], "abc"))  # Output: True
