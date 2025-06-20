"""
186. Reverse Words in a String II
https://leetcode.com/problems/reverse-words-in-a-string-ii/

Given a character array s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Constraints:
- 1 <= s.length <= 10^4
- s[i] is an English letter, digit, or space.
- There is at least one word in s.
- s does not contain leading or trailing spaces.
- All the words are separated by a single space.

Example 1:
Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Example 2:
Input: s = ["a"]
Output: ["a"]
"""
def reverseWords(s):
    def reverse(l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    n = len(s)
    reverse(0, n - 1)
    start = 0
    for i in range(n + 1):
        if i == n or s[i] == ' ':
            reverse(start, i - 1)
            start = i + 1

# Example usage:
if __name__ == "__main__":
    arr = list("the sky is blue")
    reverseWords(arr)
    print(arr)  # Output: ['b','l','u','e',' ','i','s',' ','s','k','y',' ','t','h','e']
