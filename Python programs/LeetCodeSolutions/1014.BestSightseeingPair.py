"""
1014. Best Sightseeing Pair

Given an array A of positive integers, find the maximum score of a pair of sightseeing spots, where the score of the pair (i < j) is A[i] + A[j] + i - j.

Constraints:
- 2 <= A.length <= 50,000
- 1 <= A[i] <= 1000

Example:
Input: A = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
"""
from typing import List

def maxScoreSightseeingPair(A: List[int]) -> int:
    res = 0
    max_ai = A[0]
    for j in range(1, len(A)):
        res = max(res, max_ai + A[j] - j)
        max_ai = max(max_ai, A[j] + j)
    return res

# Example usage:
A = [8,1,5,2,6]
print(maxScoreSightseeingPair(A))  # Output: 11
