"""
LeetCode 1960. Maximum Product of the Length of Two Palindromic Substrings

Given a string s, return the maximum product of the lengths of two non-overlapping palindromic substrings.

Example:
Input: s = "ababbb"
Output: 9

Constraints:
- 2 <= s.length <= 10^5
- s consists of lowercase English letters.
"""

def maxProduct(s):
    n = len(s)
    l, r = [0]*n, [0]*n
    def manacher(s):
        A = '@#' + '#'.join(s) + '#$'
        Z = [0]*len(A)
        center = right = 0
        for i in range(1, len(A)-1):
            if i < right:
                Z[i] = min(right-i, Z[2*center-i])
            while A[i+Z[i]+1] == A[i-Z[i]-1]:
                Z[i] += 1
            if i+Z[i] > right:
                center, right = i, i+Z[i]
        return Z
    Z = manacher(s)
    for i in range(n):
        l[i] = max(l[i-1] if i else 0, (Z[2*i+2]//2)*2+1 if Z[2*i+2]%2==0 else Z[2*i+2])
    Z = manacher(s[::-1])
    for i in range(n):
        r[n-i-1] = max(r[n-i] if i else 0, (Z[2*i+2]//2)*2+1 if Z[2*i+2]%2==0 else Z[2*i+2])
    res = 0
    for i in range(n-1):
        res = max(res, l[i]*r[i+1])
    return res

# Example usage:
# print(maxProduct("ababbb"))  # Output: 9
