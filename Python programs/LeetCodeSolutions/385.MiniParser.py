"""
385. Mini Parser

Given a string s representing a nested list of integers, implement a parser to deserialize it.

Constraints:
- s consists of digits, square brackets "[]", negative sign '-', and commas ','.
- 1 <= s.length <= 5 * 10^4
"""
class NestedInteger:
    def __init__(self, value=None):
        self.value = value
        self.list = []
    def isInteger(self):
        return self.value is not None
    def add(self, elem):
        self.list.append(elem)
    def setInteger(self, value):
        self.value = value
    def getInteger(self):
        return self.value
    def getList(self):
        return self.list

class Solution:
    def deserialize(self, s: str) -> 'NestedInteger':
        if not s:
            return None
        if s[0] != '[':
            return NestedInteger(int(s))
        stack, num, negative = [], 0, False
        for i, c in enumerate(s):
            if c == '-':
                negative = True
            elif c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append(NestedInteger())
            elif c in ',]':
                if s[i-1].isdigit():
                    if negative:
                        num = -num
                    stack[-1].add(NestedInteger(num))
                num, negative = 0, False
                if c == ']' and len(stack) > 1:
                    ni = stack.pop()
                    stack[-1].add(ni)
        return stack[0]

# Example usage:
s = "[123,[456,[789]]]"
obj = Solution().deserialize(s)
# Output: NestedInteger object representing the nested list
