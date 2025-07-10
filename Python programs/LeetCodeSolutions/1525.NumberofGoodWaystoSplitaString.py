"""
LeetCode 1525. Number of Good Ways to Split a String

Given a string s, return the number of good ways to split s. A good way is a split where the number of unique characters in the left and right substrings are equal.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only lowercase English letters.

Example:
Input: s = "aacaba"
Output: 2
"""
def numSplits(s):
    left, right = [0]*26, [0]*26
    unique_left = unique_right = 0
    for c in s:
        idx = ord(c) - ord('a')
        if right[idx] == 0:
            unique_right += 1
        right[idx] += 1
    res = 0
    for c in s[:-1]:
        idx = ord(c) - ord('a')
        if left[idx] == 0:
            unique_left += 1
        left[idx] += 1
        right[idx] -= 1
        if right[idx] == 0:
            unique_right -= 1
        if unique_left == unique_right:
            res += 1
    return res

# Example usage:
s = "aacaba"
print(numSplits(s))  # Output: 2
