"""
LeetCode 1759. Count Number of Homogenous Substrings

Given a string s, return the number of homogenous substrings modulo 10^9+7.

Example 1:
Input: s = "abbcccaa"
Output: 13

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase letters
"""

def countHomogenous(s):
    MOD = 10**9+7
    res = 0
    count = 1
    for i in range(1, len(s)+1):
        if i < len(s) and s[i] == s[i-1]:
            count += 1
        else:
            res = (res + count * (count+1) // 2) % MOD
            count = 1
    return res

# Example usage:
# s = "abbcccaa"
# print(countHomogenous(s))  # Output: 13
