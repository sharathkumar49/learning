"""
1111. Maximum Nesting Depth of Two Valid Parentheses Strings

Given a valid parentheses string seq, split it into two disjoint subsequences A and B such that both are valid parentheses strings and the maximum depth of A and B is minimized. Return an array answer where answer[i] = 0 if seq[i] is assigned to A, and answer[i] = 1 if seq[i] is assigned to B.

Constraints:
- 1 <= seq.length <= 10000
- seq consists only of '(' and ')'.

Example:
Input: seq = "(()())"
Output: [0,1,1,1,1,0]
"""
def maxDepthAfterSplit(seq: str) -> list:
    res = []
    depth = 0
    for c in seq:
        if c == '(': 
            res.append(depth % 2)
            depth += 1
        else:
            depth -= 1
            res.append(depth % 2)
    return res

# Example usage:
seq = "(()())"
print(maxDepthAfterSplit(seq))  # Output: [0, 1, 1, 1, 1, 0]
