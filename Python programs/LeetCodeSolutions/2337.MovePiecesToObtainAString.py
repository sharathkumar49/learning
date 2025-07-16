"""
LeetCode 2337. Move Pieces to Obtain a String

Given start and target, return true if you can obtain target from start by moving pieces.

Example:
Input: start = "_L__R_", target = "L___R"
Output: True

Constraints:
- 1 <= start.length == target.length <= 10^5
"""

def canChange(start, target):
    s = [(c, i) for i, c in enumerate(start) if c != '_']
    t = [(c, i) for i, c in enumerate(target) if c != '_']
    if [c for c, _ in s] != [c for c, _ in t]:
        return False
    for (c1, i1), (c2, i2) in zip(s, t):
        if c1 == 'L' and i1 < i2:
            return False
        if c1 == 'R' and i1 > i2:
            return False
    return True

# Example usage:
# print(canChange("_L__R_", "L___R"))  # Output: True
