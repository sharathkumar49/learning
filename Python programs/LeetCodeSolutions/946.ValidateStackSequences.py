"""
946. Validate Stack Sequences
https://leetcode.com/problems/validate-stack-sequences/

Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

Constraints:
- 1 <= pushed.length <= 1000
- 0 <= pushed[i], popped[i] < 1000
- pushed is a permutation of popped.

Example:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
"""
from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return not stack

# Example usage
if __name__ == "__main__":
    pushed = [1,2,3,4,5]
    popped = [4,5,3,2,1]
    print(Solution().validateStackSequences(pushed, popped))  # Output: True
