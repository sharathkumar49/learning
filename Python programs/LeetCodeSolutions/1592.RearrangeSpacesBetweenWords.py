"""
LeetCode 1592. Rearrange Spaces Between Words

Given a string text of words and spaces, rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words, and the remaining spaces at the end. Return the result string.

Example 1:
Input: text = "  this   is  a sentence "
Output: "this   is   a   sentence"

Constraints:
- 1 <= text.length <= 100
- text consists of lowercase English letters and ' '.
"""

def reorderSpaces(text):
    words = text.split()
    total_spaces = text.count(' ')
    if len(words) == 1:
        return words[0] + ' ' * total_spaces
    space_between = total_spaces // (len(words) - 1)
    extra = total_spaces % (len(words) - 1)
    return (' ' * space_between).join(words) + ' ' * extra

# Example usage:
# text = "  this   is  a sentence "
# print(reorderSpaces(text))  # Output: "this   is   a   sentence"
