"""
1047. Remove All Adjacent Duplicates In String

Given a string S, remove all adjacent duplicates in the string. The final string should not contain any adjacent duplicates.

Constraints:
- 1 <= S.length <= 20000
- S consists of lowercase English letters.

Example:
Input: S = "abbaca"
Output: "ca"
"""
def removeDuplicates(S: str) -> str:
    stack = []
    for c in S:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)

# Example usage:
S = "abbaca"
print(removeDuplicates(S))  # Output: "ca"
