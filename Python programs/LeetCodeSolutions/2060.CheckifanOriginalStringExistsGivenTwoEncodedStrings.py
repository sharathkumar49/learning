"""
LeetCode 2060. Check if an Original String Exists Given Two Encoded Strings

Given two encoded strings s1 and s2, return true if there exists an original string that could be encoded as both s1 and s2.

Example:
Input: s1 = "internationalization", s2 = "i18n"
Output: true

Constraints:
- 1 <= s1.length, s2.length <= 100
- s1 and s2 consist of lowercase English letters and digits.
"""

def possiblyEquals(s1, s2):
    from functools import lru_cache
    def get_nums(s, i):
        nums = []
        for l in range(1, 4):
            if i + l <= len(s) and s[i:i+l].isdigit():
                nums.append(int(s[i:i+l]))
        return nums
    @lru_cache(None)
    def dfs(i, j, diff):
        if i == len(s1) and j == len(s2):
            return diff == 0
        if i < len(s1) and s1[i].isdigit():
            for num in get_nums(s1, i):
                if dfs(i+len(str(num)), j, diff+num):
                    return True
        elif j < len(s2) and s2[j].isdigit():
            for num in get_nums(s2, j):
                if dfs(i, j+len(str(num)), diff-num):
                    return True
        elif diff > 0 and j < len(s2):
            return dfs(i, j+1, diff-1)
        elif diff < 0 and i < len(s1):
            return dfs(i+1, j, diff+1)
        elif i < len(s1) and j < len(s2) and s1[i] == s2[j]:
            return dfs(i+1, j+1, diff)
        return False
    return dfs(0, 0, 0)

# Example usage:
# print(possiblyEquals("internationalization", "i18n"))  # Output: True
