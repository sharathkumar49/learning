"""
1073. Adding Two Negabinary Numbers

Given two numbers arr1 and arr2 in base -2, return their sum, also in base -2.

Constraints:
- 1 <= arr1.length, arr2.length <= 1000
- arr1[i] and arr2[i] are 0 or 1

Example:
Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
Output: [1,0,0,0,0]
"""
from typing import List

def addNegabinary(arr1: List[int], arr2: List[int]) -> List[int]:
    i, j = len(arr1) - 1, len(arr2) - 1
    res = []
    carry = 0
    while i >= 0 or j >= 0 or carry:
        a = arr1[i] if i >= 0 else 0
        b = arr2[j] if j >= 0 else 0
        total = a + b + carry
        res.append(total & 1)
        carry = -(total >> 1)
        i -= 1
        j -= 1
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res[::-1]

# Example usage:
arr1 = [1,1,1,1,1]
arr2 = [1,0,1]
print(addNegabinary(arr1, arr2))  # Output: [1, 0, 0, 0, 0]
