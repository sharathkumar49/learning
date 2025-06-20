"""
926. Flip String to Monotone Increasing
https://leetcode.com/problems/flip-string-to-monotone-increasing/

A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).
You are given a binary string s. Return the minimum number of flips to make s monotone increasing.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either '0' or '1'.

Example:
Input: s = "00110"
Output: 1
"""
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips = ones = 0
        for c in s:
            if c == '1':
                ones += 1
            else:
                flips = min(flips + 1, ones)
        return flips

# Example usage
if __name__ == "__main__":
    s = "00110"
    print(Solution().minFlipsMonoIncr(s))  # Output: 1
