"""
1100. Find K-Length Substrings With No Repeated Characters

Given a string S and an integer K, return the number of substrings of length K with no repeated characters.

Constraints:
- 1 <= S.length <= 10^4
- 1 <= K <= S.length

Example:
Input: S = "havefunonleetcode", K = 5
Output: 6
"""
def numKLenSubstrNoRepeats(S: str, K: int) -> int:
    count = 0
    seen = set()
    left = 0
    for right in range(len(S)):
        while S[right] in seen:
            seen.remove(S[left])
            left += 1
        seen.add(S[right])
        if right - left + 1 == K:
            count += 1
            seen.remove(S[left])
            left += 1
    return count

# Example usage:
S = "havefunonleetcode"
K = 5
print(numKLenSubstrNoRepeats(S, K))  # Output: 6
