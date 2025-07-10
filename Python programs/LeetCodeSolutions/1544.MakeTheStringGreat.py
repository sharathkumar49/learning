"""
LeetCode 1544. Make The String Great

Given a string s, return the string after making it good. A string is good if no two adjacent characters have the same letter but different cases.

Constraints:
- 1 <= s.length <= 100
- s consists of only lower and upper case English letters.

Example:
Input: s = "leEeetcode"
Output: "leetcode"
"""
def makeGood(s):
    stack = []
    for c in s:
        if stack and abs(ord(stack[-1]) - ord(c)) == 32:
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)

# Example usage:
s = "leEeetcode"
print(makeGood(s))  # Output: "leetcode"
