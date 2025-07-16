"""
LeetCode 2269. Find the K-Beauty of a Number

Given num and k, return the k-beauty of num.

Example:
Input: num = 240, k = 2
Output: 2

Constraints:
- 1 <= num <= 10^9
- 1 <= k <= len(str(num))
"""

def divisorSubstrings(num, k):
    s = str(num)
    res = 0
    for i in range(len(s)-k+1):
        val = int(s[i:i+k])
        if val and num % val == 0:
            res += 1
    return res

# Example usage:
# print(divisorSubstrings(240, 2))  # Output: 2
