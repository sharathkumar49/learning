"""
LeetCode 696. Count Binary Substrings

Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Example 1:
Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011" and "01".

Example 2:
Input: s = "10101"
Output: 4

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either '0' or '1'.
"""
def countBinarySubstrings(s: str) -> int:
    prev = cur = res = 0
    last = ''
    for c in s:
        if c != last:
            res += min(prev, cur)
            prev, cur = cur, 1
            last = c
        else:
            cur += 1
    res += min(prev, cur)
    return res

# Example usage
if __name__ == "__main__":
    print(countBinarySubstrings("00110011"))  # Output: 6
    print(countBinarySubstrings("10101"))    # Output: 4
