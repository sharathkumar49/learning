"""
LeetCode 2313. Minimum Flips in Binary String to Make Substring Equal

Given s, k, return the minimum number of flips to make every substring of length k equal.

Example:
Input: s = "101101", k = 2
Output: 2

Constraints:
- 1 <= s.length <= 10^5
- 1 <= k <= s.length
"""

def minimumFlips(s, k):
    flips = 0
    s = list(s)
    for i in range(len(s)-k+1):
        if s[i] == '0':
            for j in range(k):
                s[i+j] = '1' if s[i+j] == '0' else '0'
            flips += 1
    return flips

# Example usage:
# print(minimumFlips("101101", 2))  # Output: 2
