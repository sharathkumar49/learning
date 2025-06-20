"""
214. Shortest Palindrome
https://leetcode.com/problems/shortest-palindrome/

Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Return the shortest palindrome you can find by performing this transformation.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of lowercase English letters only.

Example 1:
Input: s = "aacecaaa"
Output: "aaacecaaa"

Example 2:
Input: s = "abcd"
Output: "dcbabcd"
"""
def shortestPalindrome(s):
    rev = s[::-1]
    for i in range(len(s)+1):
        if s.startswith(rev[i:]):
            return rev[:i] + s
    return ""

# Example usage:
if __name__ == "__main__":
    print(shortestPalindrome("aacecaaa"))  # Output: "aaacecaaa"
    print(shortestPalindrome("abcd"))      # Output: "dcbabcd"
