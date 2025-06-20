"""
345. Reverse Vowels of a String

Given a string s, reverse only the vowels of a string.

Constraints:
- 1 <= s.length <= 3 * 10^5
- s consists of printable ASCII characters.
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)

# Example usage:
s = "hello"
print(Solution().reverseVowels(s))  # Output: "holle"
