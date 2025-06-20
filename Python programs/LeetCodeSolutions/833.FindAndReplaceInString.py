"""
833. Find And Replace in String

You are given a string S, and arrays indexes, sources, and targets. Perform replacements in S at the given indexes if the substring matches the source.

Example 1:
Input: S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]
Output: "eeebffff"

Constraints:
- 1 <= S.length <= 1000
- 0 <= indexes.length == sources.length == targets.length <= 100
- 0 <= indexes[i] < S.length
- All indexes[i] are distinct.
"""
def findReplaceString(S, indexes, sources, targets):
    match = {i: (s, t) for i, s, t in zip(indexes, sources, targets)}
    res = []
    i = 0
    while i < len(S):
        if i in match and S.startswith(match[i][0], i):
            res.append(match[i][1])
            i += len(match[i][0])
        else:
            res.append(S[i])
            i += 1
    return ''.join(res)

# Example usage:
print(findReplaceString("abcd", [0,2], ["a","cd"], ["eee","ffff"]))  # Output: "eeebffff"
