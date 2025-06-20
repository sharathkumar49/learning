"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.

Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true
"""
def isPalindrome(s: str) -> bool:
    filtered = [c.lower() for c in s if c.isalnum()]
    return filtered == filtered[::-1]

# Example usage:
if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
    print(isPalindrome("race a car"))                      # Output: False
