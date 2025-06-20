"""
151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/

Given an input string s, reverse the order of the words.

Constraints:
- 1 <= s.length <= 10^4
- s contains English letters (upper-case and lower-case), digits, and spaces ' '.
- There is at least one word in s.

Example:
Input: s = "the sky is blue"
Output: "blue is sky the"
"""
def reverseWords(s: str) -> str:
    return ' '.join(reversed(s.split()))

# Example usage:
if __name__ == "__main__":
    print(reverseWords("the sky is blue"))  # Output: "blue is sky the"
    print(reverseWords("  hello world  "))  # Output: "world hello"
