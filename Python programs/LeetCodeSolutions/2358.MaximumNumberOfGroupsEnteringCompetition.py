"""
LeetCode 2358. Maximum Number of Groups Entering Competition

Given grades, return the maximum number of groups that can enter the competition.

Example:
Input: grades = [10,6,12,7,3,5]
Output: 3

Constraints:
- 1 <= grades.length <= 10^5
"""

def maximumGroups(grades):
    n = len(grades)
    k = 0
    while (k+1)*(k+2)//2 <= n:
        k += 1
    return k

# Example usage:
# print(maximumGroups([10,6,12,7,3,5]))  # Output: 3
