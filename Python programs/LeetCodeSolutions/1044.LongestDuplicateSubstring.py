"""
1044. Longest Duplicate Substring

Given a string S, return the longest duplicated substring (i.e., a substring that appears at least twice). If no such substring exists, return "".

Constraints:
- 1 <= S.length <= 3 * 10^4
- S consists of lowercase English letters.

Example:
Input: S = "banana"
Output: "ana"
"""
def longestDupSubstring(S: str) -> str:
    n = len(S)
    nums = [ord(c) - ord('a') for c in S]
    mod = 2**63 - 1
    def search(L):
        h = 0
        for i in range(L):
            h = (h * 26 + nums[i]) % mod
        seen = {h}
        aL = pow(26, L, mod)
        for start in range(1, n - L + 1):
            h = (h * 26 - nums[start - 1] * aL + nums[start + L - 1]) % mod
            if h in seen:
                return start
            seen.add(h)
        return -1
    left, right = 1, n
    start = -1
    while left < right:
        mid = (left + right) // 2
        idx = search(mid)
        if idx != -1:
            left = mid + 1
            start = idx
        else:
            right = mid
    return S[start:start + left - 1] if start != -1 else ""

# Example usage:
S = "banana"
print(longestDupSubstring(S))  # Output: "ana"
