"""
LeetCode 2000. Reverse Prefix of Word

Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If ch does not exist in word, return word.

Example:
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"

Constraints:
- 1 <= word.length <= 250
- word consists of lowercase English letters.
- ch is a lowercase English letter.
"""

def reversePrefix(word, ch):
    idx = word.find(ch)
    if idx == -1:
        return word
    return word[:idx+1][::-1] + word[idx+1:]

# Example usage:
# print(reversePrefix("abcdefd", "d"))  # Output: "dcbaefd"
