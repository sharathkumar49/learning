"""
LeetCode 2085. Count Common Words With One Occurrence

Given two string arrays words1 and words2, return the number of strings that appear exactly once in each array.

Example:
Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2

Constraints:
- 1 <= words1.length, words2.length <= 1000
- 1 <= words1[i], words2[i].length <= 30
"""

def countWords(words1, words2):
    from collections import Counter
    c1 = Counter(words1)
    c2 = Counter(words2)
    return sum(c1[w] == c2[w] == 1 for w in c1)

# Example usage:
# print(countWords(["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"]))  # Output: 2
