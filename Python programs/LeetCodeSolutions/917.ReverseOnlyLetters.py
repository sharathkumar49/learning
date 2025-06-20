"""
917. Reverse Only Letters
https://leetcode.com/problems/reverse-only-letters/

Given a string s, reverse the string according to the following rules:
- All the characters that are not English letters remain in the same position.
- All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Constraints:
- 1 <= s.length <= 100
- s consists of characters with ASCII values in the range [33, 122].
- s does not contain '"' or '\'.

Example:
Input: s = "ab-cd"
Output: "dc-ba"
"""
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        res = []
        for c in s:
            if c.isalpha():
                res.append(letters.pop())
            else:
                res.append(c)
        return ''.join(res)

# Example usage
if __name__ == "__main__":
    s = "ab-cd"
    print(Solution().reverseOnlyLetters(s))  # Output: "dc-ba"
