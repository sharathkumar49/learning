"""
LeetCode 1684. Count the Number of Consistent Strings

Given a string allowed and an array of words, return the number of consistent strings. A string is consistent if all characters are in allowed.

Example 1:
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2

Constraints:
- 1 <= words.length <= 10^4
- 1 <= allowed.length <= 26
- 1 <= words[i].length <= 10
- allowed and words[i] consist of only lowercase English letters.
"""

def countConsistentStrings(allowed, words):
    allowed = set(allowed)
    return sum(all(c in allowed for c in w) for w in words)

# Example usage:
# allowed = "ab"
# words = ["ad","bd","aaab","baa","badab"]
# print(countConsistentStrings(allowed, words))  # Output: 2
