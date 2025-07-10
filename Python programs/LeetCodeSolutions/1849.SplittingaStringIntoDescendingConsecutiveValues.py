"""
LeetCode 1849. Splitting a String Into Descending Consecutive Values

Given a string s that consists of only digits, check if it can be split into two or more non-empty substrings such that the numerical values of the substrings are in descending order and the difference between every two consecutive values is 1.

Example 1:
Input: s = "1234"
Output: False

Constraints:
- 1 <= s.length <= 20
- s consists only of digits.
"""

def splitString(s):
    def dfs(i, prev):
        if i == len(s):
            return True
        for j in range(i+1, len(s)+1):
            val = int(s[i:j])
            if val == prev - 1 and dfs(j, val):
                return True
        return False
    for i in range(1, len(s)):
        if dfs(i, int(s[:i])):
            return True
    return False

# Example usage:
# s = "1234"
# print(splitString(s))  # Output: False
