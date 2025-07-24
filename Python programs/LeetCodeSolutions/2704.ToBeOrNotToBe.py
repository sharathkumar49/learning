"""
LeetCode 2704. To Be Or Not To Be

Implement a function that checks if a value is equal to another value.

Constraints:
- 1 <= calls.length <= 10^5
"""

def expect(val):
    class Expect:
        def __init__(self, val):
            self.val = val
        def toBe(self, other):
            if self.val != other:
                raise Exception("Not Equal")
            return True
        def notToBe(self, other):
            if self.val == other:
                raise Exception("Equal")
            return True
    return Expect(val)
# Example usage:
# print(expect(5).toBe(5))      # Output: True
# print(expect(5).notToBe(3))   # Output: True
