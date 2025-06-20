"""
1085. Sum of Digits in the Minimum Number

Given an array A of positive integers, return the sum of the digits of the minimum element in the array.

Constraints:
- 1 <= A.length <= 100
- 1 <= A[i] <= 10^9

Example:
Input: A = [34,23,1,24,75,33,54,8]
Output: 1
"""
from typing import List

def sumOfDigits(A: List[int]) -> int:
    return sum(map(int, str(min(A))))

# Example usage:
A = [34,23,1,24,75,33,54,8]
print(sumOfDigits(A))  # Output: 1
