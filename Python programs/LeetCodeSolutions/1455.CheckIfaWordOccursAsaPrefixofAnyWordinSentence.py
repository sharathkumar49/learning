"""
LeetCode 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

Given a sentence that consists of some words separated by a single space, and a searchWord, return the index of the word in the sentence that has searchWord as a prefix, or -1 if no such word exists.

Constraints:
- 1 <= sentence.length <= 100
- 1 <= searchWord.length <= 10
- sentence consists of lowercase English letters and spaces.
- searchWord consists of lowercase English letters.

Example:
Input: sentence = "i love eating burger", searchWord = "burg"
Output: 4
"""
def isPrefixOfWord(sentence, searchWord):
    words = sentence.split()
    for i, word in enumerate(words, 1):
        if word.startswith(searchWord):
            return i
    return -1

# Example usage:
sentence = "i love eating burger"
searchWord = "burg"
print(isPrefixOfWord(sentence, searchWord))  # Output: 4
