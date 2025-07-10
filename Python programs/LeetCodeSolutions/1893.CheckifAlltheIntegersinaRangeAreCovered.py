"""
LeetCode 1893. Check if All the Integers in a Range Are Covered

Given a 2D array ranges and two integers left and right, return true if every integer in the interval [left, right] is covered by at least one range.

Example:
Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
Output: true

Constraints:
- 1 <= ranges.length <= 50
- 1 <= left <= right <= 50
- 1 <= ranges[i][0] <= ranges[i][1] <= 50
"""

def isCovered(ranges, left, right):
    covered = [0] * 52
    for l, r in ranges:
        for i in range(l, r+1):
            covered[i] = 1
    return all(covered[i] for i in range(left, right+1))

# Example usage:
# print(isCovered([[1,2],[3,4],[5,6]], 2, 5))  # Output: True
