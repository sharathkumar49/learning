"""
1119. Remove Vowels from a String

Given a string S, remove all vowels from it.

Constraints:
- 1 <= S.length <= 1000
- S consists of lowercase English letters.

Example:
Input: S = "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
"""
def removeVowels(S: str) -> str:
    return ''.join(c for c in S if c not in 'aeiou')

# Example usage:
S = "leetcodeisacommunityforcoders"
print(removeVowels(S))  # Output: "ltcdscmmntyfrcdrs"
