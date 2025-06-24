"""
LeetCode 1328. Break a Palindrome

Given a palindromic string palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and is the lexicographically smallest possible. Return the new string, or an empty string if not possible.

Constraints:
- 1 <= palindrome.length <= 1000
- palindrome consists of lowercase English letters only.

Example:
Input: palindrome = "abccba"
Output: "aaccba"
"""
def breakPalindrome(palindrome):
    n = len(palindrome)
    if n == 1:
        return ""
    arr = list(palindrome)
    for i in range(n//2):
        if arr[i] != 'a':
            arr[i] = 'a'
            return ''.join(arr)
    arr[-1] = 'b'
    return ''.join(arr)

# Example usage:
palindrome = "abccba"
print(breakPalindrome(palindrome))  # Output: "aaccba"
