"""
LeetCode 1816. Truncate Sentence

Given a sentence s and an integer k, return the sentence after truncating it to k words.

Example 1:
Input: s = "Hello how are you Contestant", k = 4
Output: "Hello how are you"

Constraints:
- 1 <= s.length <= 500
- 1 <= k <= s.length
- s consists of only English letters and spaces
"""

def truncateSentence(s, k):
    return ' '.join(s.split()[:k])

# Example usage:
# s = "Hello how are you Contestant"
# k = 4
# print(truncateSentence(s, k))  # Output: "Hello how are you"
