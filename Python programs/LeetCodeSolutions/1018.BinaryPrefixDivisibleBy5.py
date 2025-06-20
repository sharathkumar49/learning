"""
1018. Binary Prefix Divisible By 5

Given an array A of 0s and 1s, consider the numbers formed by the prefixes of A. Return a list of booleans answer, where answer[i] is true if the number formed by the first i+1 elements of A is divisible by 5.

Constraints:
- 1 <= A.length <= 30000
- A[i] is 0 or 1

Example:
Input: A = [0,1,1]
Output: [True, False, False]
Explanation: The prefixes are: 0, 01, 011; which are 0, 1, 3 in decimal. Only 0 is divisible by 5.
"""
from typing import List

def prefixesDivBy5(A: List[int]) -> List[bool]:
    res = []
    num = 0
    for a in A:
        num = (num * 2 + a) % 5
        res.append(num == 0)
    return res

# Example usage:
A = [0,1,1]
print(prefixesDivBy5(A))  # Output: [True, False, False]
