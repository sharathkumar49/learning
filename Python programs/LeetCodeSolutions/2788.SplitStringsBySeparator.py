"""
LeetCode 2788. Split Strings by Separator

Given words and separator, return the split strings.

Constraints:
- 1 <= words.length <= 100
"""

def splitWordsBySeparator(words, separator):
    res = []
    for w in words:
        res += [x for x in w.split(separator) if x]
    return res
# Example usage:
# print(splitWordsBySeparator(["one.two.three","four.five","six"], "."))  # Output: ['one','two','three','four','five','six']
