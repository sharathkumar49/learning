"""
LeetCode 2194. Cells in a Range on an Excel Sheet

Given two strings s and e representing the start and end cell in Excel (e.g., "A1" and "C3"), return the list of all cells in the range in lexicographical order.

Example:
Input: s = "K1", e = "L2"
Output: ["K1","K2","L1","L2"]

Constraints:
- s and e are valid Excel cell references.
"""

def cellsInRange(s):
    res = []
    for c in range(ord(s[0]), ord(s[3])+1):
        for r in range(int(s[1]), int(s[4])+1):
            res.append(f"{chr(c)}{r}")
    return res

# Example usage:
# print(cellsInRange("K1:L2"))  # Output: ["K1","K2","L1","L2"]
