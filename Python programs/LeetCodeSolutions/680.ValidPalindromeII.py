"""
LeetCode 680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
"""
def validPalindrome(s: str) -> bool:
    def is_pali(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return is_pali(i+1, j) or is_pali(i, j-1)
        i += 1
        j -= 1
    return True

# Example usage
if __name__ == "__main__":
    print(validPalindrome("aba"))   # Output: True
    print(validPalindrome("abca"))  # Output: True
    print(validPalindrome("abc"))   # Output: False
