"""
LeetCode 2311. Longest Binary Subsequence Less Than or Equal to K

Given s and k, return the length of the longest subsequence less than or equal to k.

Example:
Input: s = "1001010", k = 5
Output: 5

Constraints:
- 1 <= s.length <= 100
- 1 <= k <= 10^9
"""

def longestSubsequence(s, k):
    n = len(s)
    cnt = 0
    val = 0
    for i in range(n-1, -1, -1):
        if s[i] == '0':
            cnt += 1
        else:
            if val + (1 << (n-1-i)) <= k:
                val += (1 << (n-1-i))
                cnt += 1
    return cnt

# Example usage:
# print(longestSubsequence("1001010", 5))  # Output: 5
