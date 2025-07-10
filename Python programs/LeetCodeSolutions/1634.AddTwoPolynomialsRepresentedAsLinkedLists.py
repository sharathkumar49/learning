"""
LeetCode 1634. Add Two Polynomials Represented as Linked Lists

Given two polynomials represented as linked lists, return the sum as a linked list. Each node contains a coefficient and a power.

Example 1:
Input: poly1 = [[1,2],[2,1]], poly2 = [[3,2],[4,1]]
Output: [[4,2],[6,1]]

Constraints:
- 1 <= poly1.length, poly2.length <= 1000
- 0 <= power <= 1000
"""

def addPoly(poly1, poly2):
    from collections import defaultdict
    d = defaultdict(int)
    for c, p in poly1+poly2:
        d[p] += c
    res = [[d[p], p] for p in sorted(d, reverse=True) if d[p] != 0]
    return res

# Example usage:
# poly1 = [[1,2],[2,1]]
# poly2 = [[3,2],[4,1]]
# print(addPoly(poly1, poly2))  # Output: [[4,2],[6,1]]
