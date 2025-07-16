"""
LeetCode 2446. Determine if Two Events Have Conflict

Given two events, determine if they have a conflict.

Constraints:
- Events in format "HH:MM"
"""

def haveConflict(event1, event2):
    return max(event1[0], event2[0]) <= min(event1[1], event2[1])

# Example usage:
# print(haveConflict(["01:15","02:00"],["02:00","03:00"]))  # Output: True
