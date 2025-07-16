"""
LeetCode 2490. Circular Sentence

Given a sentence, return True if it is circular.

Constraints:
- 1 <= sentence.length <= 10^5
"""

def isCircularSentence(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if words[i][-1] != words[(i+1)%len(words)][0]:
            return False
    return True

# Example usage:
# print(isCircularSentence("leetcode exercises sound delightful"))  # Output: True
