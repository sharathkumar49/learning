"""
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Constraints:
- 1 <= ransomNote.length, magazine.length <= 10^5
- ransomNote and magazine consist of lowercase English letters.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        r, m = Counter(ransomNote), Counter(magazine)
        for c in r:
            if r[c] > m[c]:
                return False
        return True

# Example usage:
ransomNote = "a"
magazine = "b"
print(Solution().canConstruct(ransomNote, magazine))  # Output: False
