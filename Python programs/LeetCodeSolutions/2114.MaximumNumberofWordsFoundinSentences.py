"""
LeetCode 2114. Maximum Number of Words Found in Sentences

Given a list of sentences, return the maximum number of words in a single sentence.

Example:
Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks"]
Output: 6

Constraints:
- 1 <= sentences.length <= 100
- 1 <= sentences[i].length <= 100
"""

def mostWordsFound(sentences):
    return max(len(s.split()) for s in sentences)

# Example usage:
# print(mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks"]))  # Output: 6
