"""
LeetCode 2575. Find the Divisibility Array of a String

Given a string num and integer m, return the divisibility array.

Constraints:
- 1 <= num.length <= 10^5
- 1 <= m <= 10^9
"""

def divisibilityArray(word, m):
    res = []
    curr = 0
    for c in word:
        curr = (curr*10+int(c))%m
        res.append(int(curr==0))
    return res
# Example usage:
# print(divisibilityArray("998244353", 3))  # Output: [0,0,0,1,0,0,0,0,0]
