"""
LeetCode 1461. Check If a String Contains All Binary Codes of Size K

Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

Constraints:
- 1 <= s.length <= 5 * 10^5
- 1 <= k <= 20

Example:
Input: s = "00110110", k = 2
Output: true
"""
def hasAllCodes(s, k):
    seen = set()
    for i in range(len(s) - k + 1):
        seen.add(s[i:i+k])
    return len(seen) == 2 ** k

# Example usage:
s = "00110110"
k = 2
print(hasAllCodes(s, k))  # Output: True
