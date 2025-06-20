"""
157. Read N Characters Given Read4
https://leetcode.com/problems/read-n-characters-given-read4/

Given a file and a method read4, implement a method to read n characters.

Constraints:
- 1 <= n <= 1000
- The file may not be empty.

Example:
Input: file = "abc", n = 4
Output: "abc"
"""
# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

def read(buf, n):
    idx = 0
    buf4 = [''] * 4
    while idx < n:
        count = read4(buf4)
        if count == 0:
            break
        for i in range(min(count, n - idx)):
            buf[idx] = buf4[i]
            idx += 1
    return idx

# Example usage:
# Not executable as-is, as read4 is assumed to be provided by the system.
