"""
LeetCode 1297. Maximum Number of Occurrences of a Substring

Given a string s, return the maximum number of occurrences of any substring with at most maxLetters unique characters and length between minSize and maxSize.

Constraints:
- 1 <= s.length <= 10^5
- 1 <= maxLetters <= 26
- 1 <= minSize <= maxSize <= min(26, s.length)

Example:
Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
"""
def maxFreq(s, maxLetters, minSize, maxSize):
    from collections import Counter
    count = Counter()
    for i in range(len(s)-minSize+1):
        sub = s[i:i+minSize]
        if len(set(sub)) <= maxLetters:
            count[sub] += 1
    return max(count.values() or [0])

# Example usage:
s = "aababcaab"
maxLetters = 2
minSize = 3
maxSize = 4
print(maxFreq(s, maxLetters, minSize, maxSize))  # Output: 2
