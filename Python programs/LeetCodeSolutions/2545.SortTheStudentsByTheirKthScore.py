"""
LeetCode 2545. Sort the Students by Their Kth Score

Given a matrix and k, sort the students by their kth score.

Constraints:
- 1 <= score.length, score[0].length <= 10^5
"""

def sortTheStudents(score, k):
    return sorted(score, key=lambda x: -x[k])
# Example usage:
# print(sortTheStudents([[10,6,9,1],[7,5,11,2],[4,8,3,15]], 2))  # Output: [[7,5,11,2],[10,6,9,1],[4,8,3,15]]
