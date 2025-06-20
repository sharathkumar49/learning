"""
LeetCode 758. Bold Words in String

Given a string s and a list of words dict, return the string s with all substrings in dict wrapped in a bold tag <b> and </b>.
If two such substrings overlap, they should be merged into a single pair of bold tags.

Example 1:
Input: s = "abcxyz123", dict = ["abc","123"]
Output: "<b>abc</b>xyz<b>123</b>"

Example 2:
Input: s = "aaabbcc", dict = ["aaa","aab","bc"]
Output: "<b>aaabbc</b>c"

Constraints:
- 1 <= s.length <= 1000
- 0 <= dict.length <= 100
- 1 <= dict[i].length <= 100
- s and dict[i] consist of lowercase English letters and digits.
"""
from typing import List

def addBoldTag(s: str, dict: List[str]) -> str:
    n = len(s)
    bold = [False] * n
    for word in dict:
        start = s.find(word)
        while start != -1:
            for i in range(start, start+len(word)):
                bold[i] = True
            start = s.find(word, start+1)
    res = []
    i = 0
    while i < n:
        if bold[i]:
            res.append('<b>')
            while i < n and bold[i]:
                res.append(s[i])
                i += 1
            res.append('</b>')
        else:
            res.append(s[i])
            i += 1
    return ''.join(res)

# Example usage
if __name__ == "__main__":
    print(addBoldTag("abcxyz123", ["abc","123"]))  # Output: "<b>abc</b>xyz<b>123</b>"
    print(addBoldTag("aaabbcc", ["aaa","aab","bc"]))  # Output: "<b>aaabbc</b>c"
