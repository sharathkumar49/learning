"""
LeetCode 1540. Can Convert String in K Moves

Given two strings s and t of the same length and an integer k, return true if you can convert s to t by shifting each character at most k times.

Constraints:
- 1 <= s.length, t.length <= 10^5
- s.length == t.length
- 0 <= k <= 10^9

Example:
Input: s = "input", t = "ouput", k = 9
Output: True
"""
def canConvertString(s, t, k):
    if len(s) != len(t):
        return False
    count = [0]*26
    for a, b in zip(s, t):
        diff = (ord(b) - ord(a)) % 26
        if diff:
            count[diff] += 1
            if count[diff] > (k - diff) // 26 + 1:
                return False
    return True

# Example usage:
s = "input"
t = "ouput"
k = 9
print(canConvertString(s, t, k))  # Output: True
