"""
158. Read N Characters Given Read4 II - Call multiple times
https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

Given a file and a method read4, implement a method to read n characters. The method may be called multiple times.

Constraints:
- 1 <= n <= 10^4
- The file may not be empty.

Example:
Input: file = "abc", n = 4
Output: "abc"
"""
# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buf4 = [''] * 4
        self.i4 = 0
        self.n4 = 0
    def read(self, buf, n):
        idx = 0
        while idx < n:
            if self.i4 == self.n4:
                self.n4 = read4(self.buf4)
                self.i4 = 0
                if self.n4 == 0:
                    break
            while idx < n and self.i4 < self.n4:
                buf[idx] = self.buf4[self.i4]
                idx += 1
                self.i4 += 1
        return idx

# Example usage:
# Not executable as-is, as read4 is assumed to be provided by the system.
