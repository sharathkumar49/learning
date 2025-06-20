"""
1062. Longest Repeating Substring

Given a string S, return the length of the longest repeating substring. If no repeating substring exists, return 0.

Constraints:
- 1 <= S.length <= 1500
- S consists of lowercase English letters.

Example:
Input: S = "abcd"
Output: 0
"""
def longestRepeatingSubstring(S: str) -> int:
    n = len(S)
    def search(L):
        seen = set()
        for i in range(n - L + 1):
            cur = S[i:i+L]
            if cur in seen:
                return True
            seen.add(cur)
        return False
    left, right = 1, n
    res = 0
    while left <= right:
        mid = (left + right) // 2
        if search(mid):
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res

# Example usage:
S = "abcd"
print(longestRepeatingSubstring(S))  # Output: 0
