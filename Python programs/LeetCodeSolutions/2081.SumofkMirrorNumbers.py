"""
LeetCode 2081. Sum of k-Mirror Numbers

Given integers k and n, return the sum of the first n k-mirror numbers.
A k-mirror number is a number that is a palindrome in both base 10 and base k.

Example:
Input: k = 2, n = 5
Output: 25

Constraints:
- 2 <= k <= 9
- 1 <= n <= 30
"""

def kMirror(k, n):
    def is_palindrome(x, base):
        s = []
        while x:
            s.append(x % base)
            x //= base
        return s == s[::-1]
    res, x, cnt = 0, 1, 0
    while cnt < n:
        if str(x) == str(x)[::-1] and is_palindrome(x, k):
            res += x
            cnt += 1
        x += 1
    return res

# Example usage:
# print(kMirror(2, 5))  # Output: 25
