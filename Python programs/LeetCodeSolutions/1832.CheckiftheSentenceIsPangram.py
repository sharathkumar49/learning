"""
LeetCode 1832. Check if the Sentence Is Pangram

Given a string sentence, return true if it is a pangram.

Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true

Constraints:
- 1 <= sentence.length <= 1000
- sentence consists of lowercase English letters
"""

def checkIfPangram(sentence):
    return len(set(sentence)) == 26

# Example usage:
# sentence = "thequickbrownfoxjumpsoverthelazydog"
# print(checkIfPangram(sentence))  # Output: True
