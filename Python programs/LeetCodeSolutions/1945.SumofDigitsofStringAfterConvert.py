"""
LeetCode 1945. Sum of Digits of String After Convert

Given a string s and an integer k, return the sum of digits of s after converting each letter to its position in the alphabet and repeating the process k times.

Example:
Input: s = "iiii", k = 1
Output: 36

Constraints:
- 1 <= s.length <= 100
- 1 <= k <= 10
- s consists of lowercase English letters.
"""

def getLucky(s, k):
    num = ''.join(str(ord(c)-96) for c in s)
    for _ in range(k):
        num = str(sum(int(x) for x in num))
    return int(num)

# Example usage:
# print(getLucky("iiii", 1))  # Output: 36
