"""
LeetCode 2108. Find First Palindromic String in the Array

Given an array of strings words, return the first palindromic string in the array, or an empty string if none exists.

Example:
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
"""

def firstPalindrome(words):
    for w in words:
        if w == w[::-1]:
            return w
    return ""

# Example usage:
# print(firstPalindrome(["abc","car","ada","racecar","cool"]))  # Output: "ada"
