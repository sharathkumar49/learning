"""
LeetCode 2138. Divide a String Into Groups of Size k

Given a string s and an integer k, return a list of groups of size k, padding the last group with fill if needed.

Example:
Input: s = "abcdefghi", k = 3, fill = "x"
Output: ["abc","def","ghi"]

Constraints:
- 1 <= s.length <= 100
- 1 <= k <= 100
- fill is a lowercase English letter
"""

def divideString(s, k, fill):
    res = [s[i:i+k] for i in range(0, len(s), k)]
    if len(res[-1]) < k:
        res[-1] += fill * (k - len(res[-1]))
    return res

# Example usage:
# print(divideString("abcdefghi", 3, "x"))  # Output: ["abc","def","ghi"]
