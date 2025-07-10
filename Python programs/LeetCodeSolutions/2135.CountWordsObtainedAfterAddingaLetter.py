"""
LeetCode 2135. Count Words Obtained After Adding a Letter

Given two string arrays startWords and targetWords, return the number of targetWords that can be obtained by adding a letter to a word in startWords and rearranging.

Example:
Input: startWords = ["ant","act","tack"], targetWords = ["tack","act","acti"]
Output: 2

Constraints:
- 1 <= startWords.length, targetWords.length <= 10^5
- 1 <= startWords[i].length, targetWords[i].length <= 26
"""

def wordCount(startWords, targetWords):
    s = set(''.join(sorted(w)) for w in startWords)
    res = 0
    for w in targetWords:
        for i in range(len(w)):
            t = ''.join(sorted(w[:i]+w[i+1:]))
            if t in s:
                res += 1
                break
    return res

# Example usage:
# print(wordCount(["ant","act","tack"], ["tack","act","acti"]))  # Output: 2
