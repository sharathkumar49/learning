"""
394. Decode String

Given an encoded string, return its decoded string.

Constraints:
- 1 <= s.length <= 30
- s consists of digits, letters, '[', and ']'.
- s is guaranteed to be a valid input.
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ''
        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == '[':
                stack.append((curr_str, curr_num))
                curr_str, curr_num = '', 0
            elif c == ']':
                last_str, num = stack.pop()
                curr_str = last_str + num * curr_str
            else:
                curr_str += c
        return curr_str

# Example usage:
s = "3[a2[c]]"
print(Solution().decodeString(s))  # Output: "accaccacc"
