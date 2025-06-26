"""
LeetCode 1451. Rearrange Words in a Sentence

Given a sentence text, rearrange the words in the sentence by the length of the words in ascending order. If two words have the same length, keep their original order.

Constraints:
- 1 <= text.length <= 10^5
- text consists of lowercase English letters and spaces.
- text has no leading or trailing spaces.
- All the words in text are separated by a single space.

Example:
Input: text = "Leetcode is cool"
Output: "is cool Leetcode"
"""
def arrangeWords(text):
    words = text.split()
    words.sort(key=len)
    res = ' '.join(words)
    return res.capitalize()

# Example usage:
text = "Leetcode is cool"
print(arrangeWords(text))  # Output: "Is cool Leetcode"
