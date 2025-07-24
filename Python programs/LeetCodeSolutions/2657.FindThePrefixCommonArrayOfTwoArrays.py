"""
LeetCode 2657. Find the Prefix Common Array of Two Arrays

Given A and B, return the prefix common array.

Constraints:
- 1 <= A.length == B.length <= 50
"""

def findThePrefixCommonArray(A, B):
    s, res = set(), []
    for a, b in zip(A, B):
        s.add(a)
        s.add(b)
        res.append(len(s & set(A[:len(res)+1]) & set(B[:len(res)+1])))
    return res
# Example usage:
# print(findThePrefixCommonArray([1,3,2,4],[3,1,2,4]))  # Output: [0,2,3,4]
