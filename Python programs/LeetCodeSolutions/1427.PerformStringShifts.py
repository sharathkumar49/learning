"""
LeetCode 1427. Perform String Shifts

Given a string s and a list of shift operations, return the final string after all shifts. Each shift operation is a pair [direction, amount]: 0 for left shift, 1 for right shift.

Constraints:
- 1 <= s.length <= 100
- 1 <= shift.length <= 100
- shift[i].length == 2
- 0 <= shift[i][0] <= 1
- 0 <= shift[i][1] <= 100

Example:
Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
"""
def stringShift(s, shift):
    total = 0
    for d, a in shift:
        total += a if d == 1 else -a
    total %= len(s)
    return s[-total:] + s[:-total] if total else s

# Example usage:
s = "abc"
shift = [[0,1],[1,2]]
print(stringShift(s, shift))  # Output: "cab"
