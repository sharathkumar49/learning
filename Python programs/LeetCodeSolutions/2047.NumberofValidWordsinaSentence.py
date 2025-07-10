"""
LeetCode 2047. Number of Valid Words in a Sentence

Given a sentence, return the number of valid words in it. A valid word contains only lowercase letters, at most one hyphen, and at most one punctuation mark at the end.

Example:
Input: sentence = "cat and  dog"
Output: 3

Constraints:
- 1 <= sentence.length <= 1000
- sentence consists of lowercase English letters, spaces, and punctuation.
"""

def countValidWords(sentence):
    import re
    tokens = sentence.split()
    cnt = 0
    for token in tokens:
        if re.fullmatch(r'[a-z]+(-[a-z]+)?[!.,]?|[a-z]+[!.,]?|[!.,]', token):
            cnt += 1
    return cnt

# Example usage:
# print(countValidWords("cat and  dog"))  # Output: 3
