"""
848. Shifting Letters

You are given a string s and an integer array shifts. Shift s[i] by shifts[i] + shifts[i+1] + ... + shifts[n-1] positions. Return the final string after all shifts.

Example 1:
Input: s = "abc", shifts = [3,5,9]
Output: "rpl"

Constraints:
- 1 <= s.length == shifts.length <= 10^5
- 0 <= shifts[i] <= 10^9
"""
def shiftingLetters(s, shifts):
    n = len(s)
    res = []
    total = 0
    for shift in reversed(shifts):
        total = (total + shift) % 26
        res.append(total)
    res = res[::-1]
    return ''.join(chr((ord(c) - ord('a') + res[i]) % 26 + ord('a')) for i, c in enumerate(s))

# Example usage:
print(shiftingLetters("abc", [3,5,9]))  # Output: "rpl"
