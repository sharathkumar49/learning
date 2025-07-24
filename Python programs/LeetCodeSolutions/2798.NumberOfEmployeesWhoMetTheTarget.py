"""
LeetCode 2798. Number of Employees Who Met the Target

Given hours and target, return the number of employees who met the target.

Constraints:
- 1 <= hours.length <= 100
"""

def numberOfEmployeesWhoMetTarget(hours, target):
    return sum(h >= target for h in hours)
# Example usage:
# print(numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2))  # Output: 3
