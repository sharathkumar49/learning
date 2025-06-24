"""
1133. Largest Unique Number

Given an array of integers, return the largest integer that only occurs once. If no such integer exists, return -1.

Constraints:
- 1 <= A.length <= 2000
- 0 <= A[i] <= 1000

Example:
Input: A = [5,7,3,9,4,9,8,3,1]
Output: 8
"""
from typing import List
from collections import Counter

def largestUniqueNumber(A: List[int]) -> int:
    count = Counter(A)
    res = -1
    for num in count:
        if count[num] == 1:
            res = max(res, num)
    return res

# Example usage:
A = [5,7,3,9,4,9,8,3,1]
print(largestUniqueNumber(A))  # Output: 8
