"""
LeetCode 1859. Sorting the Sentence

A sentence is a list of words joined by a single space, but each word is suffixed with a number. Reorder the words in the sentence based on their suffix numbers and return the sorted sentence.

Example 1:
Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"

Constraints:
- 2 <= s.length <= 200
- s consists of lowercase and uppercase English letters, spaces, and digits from 1 to 9.
- The number of words in s is between 1 and 9.
"""

def sortSentence(s):
    words = s.split()
    words.sort(key=lambda w: int(w[-1]))
    return ' '.join(w[:-1] for w in words)

# Example usage:
s = "is2 sentence4 This1 a3"
print(sortSentence(s))  # Output: "This is a sentence"
