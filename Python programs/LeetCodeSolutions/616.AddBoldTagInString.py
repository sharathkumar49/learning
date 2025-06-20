"""
616. Add Bold Tag in String
Difficulty: Medium

You are given a string s and an array of strings words. You need to wrap substrings in s that exist in words with <b> and </b> tags. If two such substrings overlap, wrap them together with only one pair of <b> and </b> tags. Return the resulting string.

Example 1:
Input: s = "abcxyz123", words = ["abc","123"]
Output: "<b>abc</b>xyz<b>123</b>"

Example 2:
Input: s = "aaabbcc", words = ["aaa","aab","bc"]
Output: "<b>aaabbc</b>c"

Constraints:
1 <= s.length <= 1000
0 <= words.length <= 100
1 <= words[i].length <= 100
s and words[i] consist of lowercase English letters.
"""

def addBoldTag(s, words):
    n = len(s)
    bold = [False] * n
    for word in words:
        start = s.find(word)
        while start != -1:
            for i in range(start, start + len(word)):
                bold[i] = True
            start = s.find(word, start + 1)
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
