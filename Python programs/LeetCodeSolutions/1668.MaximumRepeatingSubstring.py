"""
LeetCode 1668. Maximum Repeating Substring

Given a string sequence and a word, return the maximum number k such that word repeated k times is a substring of sequence.

Example 1:
Input: sequence = "ababc", word = "ab"
Output: 2

Constraints:
- 1 <= sequence.length <= 100
- 1 <= word.length <= 100
- sequence and word consist of lowercase English letters.
"""

def maxRepeating(sequence, word):
    k = 0
    while word*(k+1) in sequence:
        k += 1
    return k

# Example usage:
# sequence = "ababc"
# word = "ab"
# print(maxRepeating(sequence, word))  # Output: 2
