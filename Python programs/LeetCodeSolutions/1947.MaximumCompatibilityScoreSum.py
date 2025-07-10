"""
LeetCode 1947. Maximum Compatibility Score Sum

Given two lists of students' answers, return the maximum compatibility score sum.

Example:
Input: students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]
Output: 8

Constraints:
- m == students.length == mentors.length
- n == students[i].length == mentors[i].length
- 1 <= m, n <= 8
- students[i][j], mentors[i][j] is 0 or 1
"""

from itertools import permutations

def maxCompatibilitySum(students, mentors):
    m, n = len(students), len(students[0])
    def score(a, b):
        return sum(x == y for x, y in zip(a, b))
    return max(sum(score(students[i], mentors[j]) for i, j in enumerate(p)) for p in permutations(range(m)))

# Example usage:
# print(maxCompatibilitySum([[1,1,0],[1,0,1],[0,0,1]], [[1,0,0],[0,0,1],[1,1,0]]))  # Output: 8
